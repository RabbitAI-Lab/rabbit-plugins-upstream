## Description:

Configures GitHub Actions CI/CD workflows for testing, linting, and deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up or update GitHub Actions workflows for testing, linting, type checking, builds, publishing, and deployment in Python, Rust, or TypeScript projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or updated GitHub Actions workflows may alter CI/CD behavior, including deployment or publishing steps.

Mitigation: Review proposed workflow files before committing them, with special attention to deployment and publishing jobs.

Risk: Inline shell commands in workflow files can mask failing commands when pipelines are not configured carefully.

Mitigation: Use explicit exit-code handling or set -eo pipefail in inline workflow scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-workflow-setup)
- [claude-night-market attune plugin](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [Publisher profile](https://clawhub.ai/user/athola)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with YAML, Python, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose creating or updating files under .github/workflows.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
