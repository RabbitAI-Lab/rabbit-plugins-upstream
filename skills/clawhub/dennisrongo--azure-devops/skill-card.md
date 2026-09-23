## Description:

Helps agents work with Azure DevOps work items and pull requests using the Azure CLI and configured organization, project, reviewer, and branch settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to list assigned Azure DevOps work items, read work item details and screenshots, and prepare pull requests with configured project defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A repository-local Azure DevOps config can choose the Azure CLI executable path.

Mitigation: Use the skill only in trusted repositories, prefer a user-level Azure CLI path, and review .claude/azure-devops.json before running commands.

Risk: Work item screenshots may contain private customer, production, or credential information.

Mitigation: Open and share screenshots only in appropriate environments and avoid committing Azure DevOps configuration or sensitive work item material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/azure-devops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Azure DevOps work item summaries, attachment viewing status, pull request details, and verification notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
