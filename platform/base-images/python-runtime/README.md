# Enterprise Python Runtime Base Image

## Purpose
Approved runtime base image for Python-based microservices in the enterprise devops lab.

## Ownership
Maintained by the Platform Team.

## Intended usage
This image is intended for application runtime only.
Application services should inherit from this image instead of defining their own arbitrary Python runtime.

## Features
- Python 3 runtime
- Non-root execution
- Standard working directory: `/app`
- OCI metadata labels

## Versioning
Base images are versioned by the platform team.
Services must pin an approved version, for example:

```dockerfile
FROM <ECR>/enterprise/python-runtime:1.0.0
