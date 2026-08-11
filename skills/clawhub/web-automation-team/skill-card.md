## Description:

Automates browser tasks across roles to map sites, plan and execute workflows, and verify results on sites without usable APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this agent configuration bundle to coordinate browser-based research, workflow execution, and review for sites that do not provide a usable API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation may operate on sensitive logged-in sites or perform actions beyond simple information gathering.

Mitigation: Keep browser actions under normal user approval controls and avoid sensitive logged-in sites unless the task clearly requires them.

Risk: The bundle can use memory, file writes, and MCP invocation while coordinating research and review work.

Mitigation: Run it in a scoped workspace, review file changes before use, and grant only the tools and site access needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/web-automation-team)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text guidance with optional shell commands and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the delegated browser, research, and review roles.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
