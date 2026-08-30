## Description:

Azure DevOps helps agents use the Azure CLI to query assigned or sprint work items, read work item details and screenshots, publish branches, and create pull requests with configured reviewers, work-item links, and auto-complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate against Azure DevOps projects from an agent session: listing assigned work, reading work items and attachments, and preparing pull requests with local team defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create pull requests, set reviewers, enable auto-complete, and push branches when the user asks it to perform release workflow actions.

Mitigation: Confirm branch pushes, PR creation, reviewer changes, work-item links, and auto-complete settings before allowing the agent to execute those operations.

Risk: The skill reads and may offer to write Azure DevOps organization, project, reviewer, and CLI path settings.

Mitigation: Review `.claude/azure-devops.json` before use and prefer repo-local configuration when working across different tenants or projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/azure-devops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Azure DevOps work item summaries, attachment-viewing status, pull request URLs, verification results, and configuration recommendations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
