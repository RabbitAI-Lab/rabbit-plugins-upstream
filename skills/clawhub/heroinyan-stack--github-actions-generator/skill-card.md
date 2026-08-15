## Description:

Generates GitHub Actions workflow YAML for CI, deployment, release automation, security scanning, caching, matrix builds, and related setup checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to create GitHub Actions workflows for linting, testing, building, scanning, deploying, and releasing projects based on repository stack signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated deployment workflows may request permissions, secrets, environments, cloud role names, or third-party actions that do not match the target repository's security requirements.

Mitigation: Review generated workflow YAML before committing it, with particular attention to permissions blocks, OIDC role assumptions, secrets, environment approval gates, and third-party actions.

Risk: Broad activation wording could route generic CI/CD requests to a GitHub Actions-specific generator.

Mitigation: Confirm the user wants GitHub Actions workflows before applying the generated guidance or YAML.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/github-actions-generator)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with GitHub Actions YAML code blocks and secrets, variables, and environment checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated workflows should be reviewed before committing, especially permissions, secrets, deployment environments, cloud role names, and third-party actions.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
