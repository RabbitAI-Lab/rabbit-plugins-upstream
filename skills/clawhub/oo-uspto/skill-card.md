## Description:

USPTO (uspto.gov). Use this skill for USPTO requests involving reading, creating, and updating data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and trademark operations teams use this skill to run USPTO trademark lookups through an OOMOL-connected account. It supports case status, last update date, and document metadata retrieval by trademark application serial number.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Use an independently verified and pinned oo CLI installation method before running connector commands.

Risk: The skill includes a write-tagged USPTO action.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any write-tagged action.

Risk: USPTO actions run through an OOMOL-connected account and may depend on account connection, scopes, credentials, or billing status.

Mitigation: Confirm the intended OOMOL connection and stop on authentication, scope, credential, or billing errors until the user resolves them.

## Reference(s):

- [ClawHub USPTO skill page](https://clawhub.ai/oomol/skills/oo-uspto)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [USPTO homepage](https://www.uspto.gov/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target OOMOL oo CLI connector actions and may return JSON or XML USPTO data.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
