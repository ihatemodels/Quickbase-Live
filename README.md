# Quickbase Live

[![Spellcheck](https://github.com/ihatemodels/Quickbase-Live/actions/workflows/spellcheck.yml/badge.svg)](https://github.com/ihatemodels/Quickbase-Live/actions/workflows/spellcheck.yml)
[![Rufflint](https://github.com/ihatemodels/Quickbase-Live/actions/workflows/ruff.yml/badge.svg)](https://github.com/ihatemodels/Quickbase-Live/actions/workflows/ruff.yml)
[![Gitleaks](https://github.com/ihatemodels/Quickbase-Live/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/ihatemodels/Quickbase-Live/actions/workflows/gitleaks.yml)

<p align="center">
    <a href="https://quickbase.live" target="_blank"><img src="src/static/img/quickbase-logo-color.png" width="1000" height="130"/></a>
</p>


The goal of this project is to address a DevOps technical challenge for QB. 

## Table of Contents

- **[Application](#application)**
    - **[API](#api)**
- **[Infrastructure](#infrastructure)**
- **[CI](#ci)**
- **[Monitoring](#monitoring)**
- **[Presentation Questions](#presentation-questions)**
- **[Overextending](#overextending)**

### Application 

The task offered the option of using a prebuilt Java or Python application. However, to uniquely showcase my skills, I took the initiative to develop a static site application alongside an API using Python. Through this web-based project, I've attempt to present an engaging argument for why I'd be a valuable addition to your team.

Explore the application at https://quickbase.live (P.S.: If you hire me, I might consider selling the domain!) 😉

#### API

The api is accessible on https://quickbase.live/swagger. You can navigate to the swagger documentation and test the api from there. 

The most important endpoint is the `/api/hire-me` endpoint. This endpoint is used to show the most important information about the reviewer of this project.

Test it out yourself:

```bash
curl -X 'GET' \
  'https://quickbase.live/api/hire-me' \
  -H 'accept: application/json' | jq
```

### Infrastructure

The infrastructure for this project is constructed using Terraform, with the relevant scripts and configuration files housed in the `iac/` directory. Presently, the Terraform state is stored locally within the repository. This setup is primarily for demonstration purposes. In a real-world scenario, I would segregate the infrastructure into a distinct repository, complete with its own CI and validation processes.The infrastructure is deployed on Google Cloud Platform (GCP) and leverages the following services:

- [Cloud Run](https://cloud.google.com/run): To deploy and manage the container for our application.
- [Custom Domain Mapping](https://cloud.google.com/run/docs/mapping-custom-domains): To map the domain name to the Cloud Run service.
- [Cloud Monitoring](https://cloud.google.com/run/docs/monitoring): To monitor the Cloud Run service.

I choose to use Cloud Run because it offers a fully managed serverless environment for running containers. This allows me to focus on the application itself, rather than the underlying infrastructure. Additionally, Cloud Run is a cost-effective solution that scales automatically to meet demand. Cloud Run also offers a automatic SSL certificate management through [Let's Encrypt](https://letsencrypt.org/). This is a great feature that allows us to use HTTPS with custom domain without having to worry about certificate management.

### CI 

The Continuous Integration (CI) process is powered by GitHub Actions and the workflow configurations can be found in the `.github/workflows/` directory. While the primary task was to establish a deployment step targeting GCP, I went a step further. I've set up a comprehensive CI pipeline that offers linting, spellchecking, security scanning and more with each push and pull request to the repository. Deployment to GCP is triggered exclusively when a new tag is created from the main branch, and only after all checks have been successfully passed.

For container artifact storage, I utilize my organization's container registry on Docker Hub. You can browse the container assets from this repository at https://hub.docker.com/orgs/st3ga/repositories. As an added layer of security, I leverage Docker Hub's built-in security scanning to scrutinize the images for potential vulnerabilities. A status badge indicating the security status of the images is placed at the top of this README for quick reference.

### Monitoring

The application exposes Prometheus metrics, which are accessible at https://quickbase.live/metrics/. It's important to note that, under typical circumstances, exposing Prometheus metrics publicly is not recommended due to security considerations. However, for the purposes of this demonstration, I've made an exception.

The metrics are aggregated by a Prometheus server that I've configured within my own infrastructure to optimize costs and avoid additional expenses on GCP. To complement this, I've also developed a Grafana dashboard to visualize these metrics. Although the dashboard is part of my private setup, I am more than happy to provide a demonstration during the presentation.

Apart from that i would consider adding a logging solution to the application. This would allow for better visibility into the application's behavior. But this is not present in the current setup due to time constraints.

For the underlying infrastructure we use the Google Cloud Platform [Built-in metrics for Cloud Run](https://cloud.google.com/run/docs/monitoring)

### Presentation Questions

- **What type of steps you would perform in order to verify the deployment is successful?**

    The deployment's success on Google Cloud Run is determined by health and startup checks. A successful HTTP call to /api/healthz that returns a status code of 200 indicates a successful deployment, prompting the transition to the new version. Conversely, if this check fails, the deployment is considered unsuccessful, and the system retains the previous version.

    Additionally, our Release pipeline incorporates an automated check targeting the endpoint https://quickbase.live/api/healthz. A status code of 200, coupled with the "version" JSON field matching the VERSION file, confirms a successful deployment within the pipeline.

    Given the simplicity of this application, these measures suffice for deployment verification. However, for more intricate applications, a broader range of checks would be necessary. For instance, introducing smoke tests could further ensure the application's intended functionality post-deployment, among other potential verifications

- **Plan and a task break-down how you would implement monitoring of this deployed app**

    The monitoring for the application is already implemented. We have the following monitoring tools in place:

    - [Built-in metrics for Cloud Run](https://cloud.google.com/run/docs/monitoring)
    - [Prometheus metrics](https://quickbase.live/metrics/)
    - [Grafana dashboard](https://grafana.com/grafana/dashboards/14526)

    **Future Enhancements:**

    1. **Logging**: To further enhance observability, integrating a logging solution is paramount. This will offer deeper insights into the application's dynamics. However, due to time restrictions, logging has yet to be integrated into the current setup.

    2. **Tracing**: Implementing tracing, especially distributed tracing, will allow us to meticulously track how the application interacts with other services and infrastructure components, enabling a comprehensive understanding of its performance dynamics.

    3. **Alerting**: An integral step forward would be to introduce alerting mechanisms to our monitoring solutions. This ensures proactive issue detection by sending out notifications when anomalies arise.

    4. **External Multi Continental Site Speed Monitoring**: We can use a service like [SpeedCurve](https://speedcurve.com/) to monitor the site speed from different locations around the world. This will allow us to have a better understanding of the site speed from different locations and we can use the data to improve the site speed.

- **What kind of security policies and scans would you recommend to put into place?**

    The CI process already includes some security scans. We use: 

    - Secrets Scans

        We use [Gitleaks]() To scan for secrets left in the repository. This will prevent the pipeline to continue if a secret is found.
        So the author should fix the Git history and remove the secret from the repository. Also the secret should be revoked and a new one should be created.

    - Secure Coding Guidelines

        While our repository currently features a linter, we haven't configured specific guidelines due to time constraints. Fortunately, the default linter rules already address and mitigate several security concerns.

    - Dependency Scanning

        We use the Github dependency scanning to scan for vulnerabilities in the dependencies. It's configured to run on every pull request and it will deny the MR if the scanner detects a high and above level of security issue. The MR will fail also if the scanner detects a license of the dependency that is not allowed by our standard. Allowed Licenses and can be configured in `.github/workflows/dependa.yml`

    - Container Scanning

        We use [Trivy](https://github.com/aquasecurity/trivy) in our pipeline to scan the container for vulnerabilities. The pipeline will fail if the scanner detects a high and above level of security issue in the container asset.
    
    - Static Code Analysis/Static Program Analysis

        We use Github Code QL to scan the code for security issues. The results of the scans can be found in the [Security Tab](https://github.com/ihatemodels/Quickbase-Live/security/code-scanning) of the repository. As a feature improve we should fail the pipeline if the scanner detects a high and above level of security issue in the code at the current commit.

        
    The following security scans are not implemented but i would recommend to implement them:

    - Web Application Firewall

        We should use a WAF to protect the application from different kind of attacks that can be prevented with WAF.

- **What other improvements would you make to the CI/CD process if you had more time?**

    I will consider using the Github Release feature and integrate the pipeline with it. This will allow us to have a better control over the releases and we can use the release notes to describe the changes in the release. Also we can use the release feature to trigger the deployment to GCP.

    I will add a unit and smoke tests to the application. This will allow us to have a better confidence in the application and we can use the tests to verify the application is working as expected.

    More of the changes that i would make are described in the sections above.


### Overextending

I've gone above and beyond with this project. While I was fully aware of the initial requirements, I felt compelled to elevate the project to a standard I'd deem presentation-ready. To be candid, this approach aligns with how I'd handle a real-world scenario, especially for a Python application intended for public visibility on GitHub and hosting on GCP.