## Description:

HeyReach (heyreach.io). Use this skill for reading, creating, and updating HeyReach data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and sales operations teams use this skill to let an agent inspect HeyReach connector schemas, retrieve campaigns, leads, tags, lists, sender accounts, and outreach statistics, and create empty HeyReach lead or company lists when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may direct an agent to install the oo CLI by executing remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installer from an official source and prefer a signed or checksum-verified package before installation.

Risk: Write actions can modify HeyReach data, including creating lead or company lists.

Mitigation: Confirm the exact payload and expected effect with the user before allowing any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-heyreach)
- [HeyReach homepage](https://www.heyreach.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance, configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live HeyReach connector schemas; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
