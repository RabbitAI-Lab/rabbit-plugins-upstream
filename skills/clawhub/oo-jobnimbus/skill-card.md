## Description:

Use this skill to read, create, and update JobNimbus data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect JobNimbus connector schemas and read, create, list, retrieve, or update contacts and jobs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute changing code on a user's machine.

Mitigation: Review or manually install the oo CLI from a trusted, verified source before running installer commands.

Risk: Create and update actions can change JobNimbus business records through the connected account.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write actions.

## Reference(s):

- [JobNimbus homepage](https://www.jobnimbus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, PowerShell commands, text URLs, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live action schemas and run JobNimbus connector actions that return JSON data with execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
