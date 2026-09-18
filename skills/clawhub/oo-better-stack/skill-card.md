## Description:

Better Stack (betterstack.com). Use this skill for ANY Better Stack request - reading, creating, and updating data. Whenever a task involves Better Stack, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Better Stack action schemas and run incident, comment, and metadata actions through an OOMOL-connected Better Stack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident-changing actions may acknowledge, create, or escalate Better Stack incidents.

Mitigation: Manually confirm the exact incident, target, payload, and expected effect before running acknowledgement, creation, or escalation actions.

Risk: Remote installer commands can execute code fetched from OOMOL-hosted URLs.

Mitigation: Prefer an official package, pinned download, or installer that has been inspected and verified before execution.

Risk: The OOMOL Better Stack connector can act with the Better Stack permissions granted to it.

Mitigation: Grant the connector only the required Better Stack permissions and install the skill only when that access level is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-better-stack)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Better Stack](https://betterstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce Better Stack action schemas, command invocations, setup guidance, and connector responses when run by an agent.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
