## Description:

DialMyCalls helps agents read, create, update, and delete DialMyCalls account, contact, and group data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting DialMyCalls users use this skill to check account details and credits, retrieve contacts and groups, and manage contact or group records. It is intended for connected DialMyCalls accounts where state-changing actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes internet installer commands that security evidence flags for review before installation.

Mitigation: Verify the oo CLI using OOMOL's official installation documentation and prefer a pinned or checksum-verified installer before running setup commands.

Risk: The skill can create, update, and delete DialMyCalls contacts and groups.

Mitigation: Require explicit user confirmation for the exact target, payload, and expected effect before any create, update, or delete action.

Risk: A connected DialMyCalls account gives the agent access to account, credit, contact, and group data.

Mitigation: Use the skill only with a DialMyCalls account the user intends the agent to manage, and inspect the live action schema before constructing payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dialmycalls)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [DialMyCalls Homepage](https://www.dialmycalls.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses when executed.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
