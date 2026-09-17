## Description:

Monica CRM access for reading, creating, updating, and deleting Monica contacts and notes through the OOMOL Monica CRM connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Monica CRM through an OOMOL-connected account, including listing and retrieving contacts and creating, updating, or deleting contact notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes direct remote installer commands for the oo CLI.

Mitigation: Use an independently verified, version-pinned, or signed oo CLI installation method before enabling the skill.

Risk: Write and destructive Monica CRM actions can modify or delete contact notes.

Mitigation: Inspect the live action schema, review the exact payload and target, and require explicit user approval before write or delete actions.

Risk: Monica CRM access is mediated through OOMOL's connector.

Mitigation: Install only when the user accepts OOMOL handling Monica CRM access for this workflow.

## Reference(s):

- [ClawHub Monica CRM skill page](https://clawhub.ai/oomol/skills/oo-monica-crm)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Monica CRM homepage](https://www.monicahq.com/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
