# MLOps CI/Cd automation

This repository contains the code for a machine learning model that is automatically containerized and pushed to Docker Hub when changes are pushed to the `main` branch. It also includes testing on the `test` branch and quality checks using Flake8 on the `dev` branch.

## Repository Structure

- `main`: The main branch where the final version of the code is pushed. It triggers the containerization and deployment process.
- `test`: The branch used for testing purposes.
- `dev`: The branch used for development and code quality checks.

## CI/CD Pipeline

The CI/CD pipeline is defined in a Jenkinsfile and includes the following stages:

1. **Cloning Git Repository**: Clones the repository from GitHub.
2. **Building the Image**: Builds the Docker image from the source code.
3. **Deploying the Image**: Pushes the Docker image to Docker Hub.

## Jenkinsfile

```groovy
pipeline {
    environment {
        registryCredential = 'AbdullahDockerCredentials'
        IMAGE_NAME = 'mianabdullah/mlops-assignment1'
        TAG = 'latest' 
    }
    agent any
    stages {
        stage('Cloning Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/abdullah117765/MlopsAssignment1.git'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }
    post {
        success {
            emailext(
                to: 'axiomshah@gmail.com',
                subject: 'Build Successful',
                body: 'The docker image successfully pushed to Dockerhub! Well Done!'
            )
        }
    }
}

```

## Testing and Code Quality

### Test Branch

The `test` branch is used to run automated tests on the code. Ensure you have your test scripts set up to run when changes are pushed to this branch.

### Dev Branch

The `dev` branch is used to check code quality using Flake8. Ensure Flake8 is set up in your `dev` branch and runs as part of the CI pipeline.

## Docker Hub

The Docker image is pushed to [Docker Hub](https://hub.docker.com/repository/docker/mianabdullah/mlops-assignment1) under the `mianabdullah/mlops-assignment1` repository with the tag `latest`.

## Notifications

An email notification is sent upon successful build and deployment of the Docker image. The email is sent to `axiomshah@gmail.com` with the subject "Build Successful" and the body "The docker image successfully pushed to Dockerhub! Well Done!"

## Setup Instructions

1. **Clone the Repository**
    ```sh
    git clone https://github.com/abdullah117765/MlopsAssignment1.git
    ```
2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```
3. **Run Tests**
    ```sh
    pytest
    ```
4. **Check Code Quality**
    ```sh
    flake8 .
    ```
5. **Build and Run Docker Image Locally**
    ```sh
    docker build -t mianabdullah/mlops-assignment1:latest .
    docker run -p 8000:8000 mianabdullah/mlops-assignment1:latest
    ```

## Contributions

Feel free to open a pull request or file an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

This `README.md` file provides comprehensive instructions and information about the repository, CI/CD pipeline, and how to contribute.
