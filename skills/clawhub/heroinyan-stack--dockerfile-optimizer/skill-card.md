## Description:

Audits Dockerfiles for security issues and best practices, optimizes build performance, reduces image size, and generates compliant multi-stage Dockerfiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review Linux-container Dockerfiles, identify security and build-performance issues, and produce optimized Dockerfile and .dockerignore content with before/after explanations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Dockerfile changes can alter build behavior, runtime dependencies, or deployment compatibility if applied without review.

Mitigation: Review each generated Dockerfile change, test the resulting image in CI, and confirm base image recommendations against project and organization requirements.

Risk: Generated .dockerignore content can accidentally exclude required files or fail to exclude sensitive build-context files.

Mitigation: Compare the proposed .dockerignore against the application's required build inputs and secret-handling policy before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/dockerfile-optimizer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Dockerfile, .dockerignore, report tables, and inline shell command code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes before/after comparisons, severity-labeled security findings, and rationale for each recommended change.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
