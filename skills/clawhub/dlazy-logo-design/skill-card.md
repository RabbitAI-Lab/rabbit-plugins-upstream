## Description:

Helps users create, upgrade, or evaluate logos and brand identity, delivering transparent-background marks with multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and other users can use the skill to create a logo, refine an existing mark, or evaluate a brand identity. It guides the work through the dLazy logo-design service and returns logo assets with multi-context previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services, and CLI login saves an API key in the local user configuration.

Mitigation: Review prompts and attachments for sensitive information before sending them, and use an API key you can rotate or revoke from the dLazy dashboard.

Risk: Broad activation terms and project-listing behavior may lead to an unintended CLI task or project being selected.

Mitigation: Confirm the task and project ID before running a command, and review the requested action when the skill is triggered by an ambiguous prompt.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [Project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [Skill release page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)

## Skill Output:

**Output Type(s):** [Image files, Text guidance]

**Output Format:** [Logo image assets with a live multi-context preview and streamed text replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Logo assets are described as having transparent backgrounds; attached reference files are uploaded for service use.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
