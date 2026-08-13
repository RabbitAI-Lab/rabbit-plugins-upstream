## Description:

Generates GitHub Actions workflows for linting, testing, building, security scanning, deployment, and release automation based on a project's stack and requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to generate GitHub Actions workflow YAML and supporting checklists for CI, security scanning, deployment, and release automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workflows may affect repository permissions, deployments, releases, secrets, or third-party action execution.

Mitigation: Review each generated workflow before committing it, scope permissions narrowly, verify secret references, and check deployment and release gates.

Risk: The skill is purpose-built for GitHub Actions and may be a poor fit for generic or non-GitHub CI/CD requests.

Mitigation: Use it for GitHub Actions workflow generation and avoid or narrow requests for unrelated CI systems.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/heroinyan-stack/skills/github-actions-generator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with GitHub Actions YAML workflow examples, shell command snippets, and setup checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated workflows should be reviewed before committing, especially permissions, secrets, deployment, release, and third-party action references.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
