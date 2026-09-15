## Description:

SmartSuite helps agents read, create, update, and delete SmartSuite workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to automate SmartSuite record and table workflows, including listing solutions, inspecting tables, and managing records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and PowerShell iex installer commands for the oo CLI.

Mitigation: Review the setup path before installing and prefer a verified, pinned, signed, or package-manager installation route.

Risk: The skill can create, update, and delete SmartSuite records.

Mitigation: Confirm the exact payload and target with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-smartsuite)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SmartSuite Homepage](https://www.smartsuite.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
