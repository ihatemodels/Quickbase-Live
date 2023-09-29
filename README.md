# qb-demo-challenge

<p align="center">
    <a href="https://seekvectorlogo.com/quick-base-vector-logo-svg/" target="_blank"><img src="https://seekvectorlogo.com/wp-content/uploads/2022/02/quick-base-vector-logo-2022.png" width="200" height="100"/></a>
</p>

[![Spellcheck](https://github.com/ihatemodels/qb-demo-challenge/actions/workflows/spellcheck.yml/badge.svg)](https://github.com/ihatemodels/qb-demo-challenge/actions/workflows/spellcheck.yml)
[![Rufflint](https://github.com/ihatemodels/qb-demo-challenge/actions/workflows/ruff.yml/badge.svg)](https://github.com/ihatemodels/qb-demo-challenge/actions/workflows/ruff.yml)
[![Gitleaks](https://github.com/ihatemodels/qb-demo-challenge/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/ihatemodels/qb-demo-challenge/actions/workflows/gitleaks.yml)

The goal of this project is to address a DevOps technical challenge for QB. 

## Table of Contents

- **[Application](#application)**
- **[Infrastructure](#infrastructure)**
- **[CI](#ci)**
- **[Monitoring](#monitoring)**
- **[Overextending](#overextending)**

### Application 

The task offered the option of using a prebuilt Java or Python application. However, to uniquely showcase my skills, I took the initiative to develop a static site application alongside an API using Python. Through this web-based project, I've attempt to present an engaging argument for why I'd be a valuable addition to your team. You can find the source code within the `src/` directory.

Explore the application at https://quickbase-demo.site (P.S.: If you hire me, I might consider selling the domain!) 😉

### Infrastructure

The infrastructure for this project is constructed using Terraform, with the relevant scripts and configuration files housed in the `iac/` directory. Presently, the Terraform state is stored locally within the repository. This setup is primarily for demonstration purposes. In a real-world scenario, I would segregate the infrastructure into a distinct repository, complete with its own CI and validation processes.The infrastructure is deployed on Google Cloud Platform (GCP) and leverages the following services:

- Cloud Run: To deploy and manage the containers for our application.
- Cloud Build: Handling CI/CD, ensuring seamless integration and deployment.
- Cloud Storage: Storing data and serving static assets for the application.

### CI 

The Continuous Integration (CI) process is powered by GitHub Actions and the workflow configurations can be found in the `.github/workflows/` directory. While the primary task was to establish a deployment step targeting GCP, I went a step further. I've set up a comprehensive CI pipeline that offers linting, spellchecking, security scanning and more with each push and pull request to the repository. Deployment to GCP is triggered exclusively when a new tag is created from the main branch, and only after all checks have been successfully passed.

For container artifact storage, I utilize my organization's container registry on Docker Hub. You can browse the collection of repositories here: https://hub.docker.com/orgs/st3ga/repositories. As an added layer of security, I leverage Docker Hub's built-in security scanning to scrutinize the images for potential vulnerabilities. A status badge indicating the security status of the images is conveniently placed at the top of this README for quick reference.

### Monitoring

The application exposes Prometheus metrics, which are accessible at https://quickbase-demo.site/metrics/. It's important to note that, under typical circumstances, exposing Prometheus metrics publicly is not recommended due to security considerations. However, for the purposes of this demonstration, I've made an exception.

The metrics are aggregated by a Prometheus server that I've configured within my own infrastructure to optimize costs and avoid additional expenses on GCP. To complement this, I've also developed a Grafana dashboard to visualize these metrics. Although the dashboard is part of my private setup, I am more than happy to provide a demonstration during the presentation.

### Overextending

I've gone above and beyond with this project. While I was fully aware of the initial requirements, I felt compelled to elevate the project to a standard I'd deem presentation-ready. To be candid, this approach aligns with how I'd handle a real-world scenario, especially for a Python application intended for public visibility on GitHub and hosting on GCP.