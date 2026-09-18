## Description:

The SMTP2GO skill lets an agent manage SMTP2GO account data through an OOMOL-connected account, including account summaries, sender verification data, activity and template searches, and standard email sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting SMTP2GO account users use this skill to inspect account and sender status, search email activity and templates, retrieve template details, view API key permissions, and send standard JSON emails after write-action confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Review before installing; prefer an official signed or version-pinned package, inspect downloaded scripts before execution, and approve any install or login step explicitly.

Risk: The send_email action can send messages through the connected SMTP2GO account.

Mitigation: Confirm the exact recipients, payload, and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-smtp2go)
- [SMTP2GO homepage](https://www.smtp2go.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command snippets and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
