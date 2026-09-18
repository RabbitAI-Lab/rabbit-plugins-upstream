## Description:

Vonage (vonage.com) skill for reading, creating, and updating Vonage data through the documented OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with a connected Vonage account through OOMOL, including checking account balance, reviewing SMS delivery records, listing SMS history, and sending SMS messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Review the installer path before use and prefer a pinned, signed, or checksum-verified official oo CLI release.

Risk: The send_sms action can send text or Unicode SMS through the connected Vonage account.

Mitigation: Confirm the exact recipient, message body, and expected effect with the user before allowing any SMS send operation.

Risk: Using actions outside the documented Vonage connector behavior could expand operational risk.

Mitigation: Use the skill only for the documented Vonage actions and inspect the live connector schema before constructing payloads.

## Reference(s):

- [ClawHub Vonage skill page](https://clawhub.ai/oomol/skills/oo-vonage)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vonage homepage](https://www.vonage.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
