## Description:

Elorus (elorus.com). Use this skill for ANY Elorus request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Elorus through an OOMOL-connected account, including listing, retrieving, creating, and updating contacts, invoices, and products or services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer one-liners that run downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI through a reviewed, version-pinned, or otherwise verified method instead of allowing an agent to run installer one-liners automatically.

Risk: Write actions can create or update Elorus contacts, invoices, and products or services.

Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged write.

Risk: The connector operates through an OOMOL-connected Elorus account with server-side credentials.

Mitigation: Use only with trusted OOMOL and Elorus accounts, and resolve authentication, connection, scope, or billing failures through deliberate user-controlled setup steps.

## Reference(s):

- [Elorus homepage](https://www.elorus.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elorus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
