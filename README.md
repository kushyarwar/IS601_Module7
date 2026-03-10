# QR Code Generator - Module 7

A Dockerized QR Code Generator application built with Python.

## DockerHub Image
https://hub.docker.com/repository/docker/kushyarwar/qr-code-generator-app/general

## How to Run

### Build the image
```
docker build -t qr-code-generator-app .
```

### Run the container
```
docker run --name qr-generator qr-code-generator-app
```

### Run with a custom URL
```
docker run --name qr-generator qr-code-generator-app --url https://example.com
```

### View logs
```
docker logs qr-generator
```

## Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| QR_URL | https://github.com/kaw393939 | URL to encode |
| QR_FILL_COLOR | black | Foreground color |
| QR_BACK_COLOR | white | Background color |
| QR_SIZE | 10 | Box size in pixels |
| QR_BORDER | 4 | Border width |

## GitHub Actions
The workflow automatically builds and pushes the Docker image to DockerHub on every push to main.

## Submission
The reflection document, container logs screenshot, and GitHub Actions workflow screenshot are all included in `Reflection_Module7.pdf`.
