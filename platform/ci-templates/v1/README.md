# CI Templates v1

## Purpose
Versioned shared CI template set for application services in the enterprise devops lab.

## Scope
This version defines the standard CI stages for service validation and artifact delivery:

- validate
- test
- build
- scan
- publish

## Ownership
The Platform Team owns and maintains the shared CI templates.
Application teams consume these templates through a versioned integration model.

## Design intent
The CI templates are centralized under the platform layer so that service teams do not implement pipeline logic independently.
This reduces delivery drift and allows CI standards to be governed centrally.

## Versioning
Service pipelines must reference a specific template version.
This prevents uncontrolled change propagation across all services.

## Delivery model
These templates define CI behavior only.
Deployment is handled separately by the CD/GitOps layer.

## Notes
This is the initial template contract.
Execution engine specifics can later be implemented using GitHub Actions or another CI system.
