## Description:

Helps open the local agent-skeleton assistant at localhost:3000, checking the service first and guiding startup or troubleshooting when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All Rights Reserved

## Use Case:

People running a local agent-skeleton assistant use this skill to check whether their local page is available, open it, or diagnose and start the service after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words may invoke the skill when the user did not intend to open the local assistant.

Mitigation: Use it only when the user explicitly wants to inspect or open the local agent-skeleton page.

Risk: Starting the local service can launch a background process or change the local environment.

Mitigation: Check the port first and obtain confirmation before startup or other environment-changing commands.

## Reference(s):

- [local-agent-open on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/local-agent-open)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local service status, startup or troubleshooting guidance, and a localhost page-opening action.]

## Skill Version(s):

1.0.2 (source: server release; bundled frontmatter says 1.0.1 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
