## Description:

Resend (resend.com). Use this skill for ANY Resend request: reading, creating, and updating data through an OOMOL-connected Resend account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Resend email activity, retrieve message and attachment details, send individual or batch emails, and manage scheduled email delivery through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute remote installer scripts directly, which may run mutable code on a user's machine.

Mitigation: Prefer a verified, version-pinned oo CLI installation path before running the skill's setup commands.

Risk: The skill can send email, send up to 100 batch emails, cancel scheduled emails, and update scheduled delivery times.

Mitigation: Confirm the exact payload and expected effect with the user before any write or batch-send action runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-resend)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Resend homepage](https://resend.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
