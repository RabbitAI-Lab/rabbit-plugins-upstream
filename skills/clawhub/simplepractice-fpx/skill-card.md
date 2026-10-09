## Description:

Guides users through read-only access to their authorized SimplePractice Client Portal records using curl, with optional browser-session capture through fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized SimplePractice portal users and developers use this skill to read appointments, billing records, documents, and practice information from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session cookies, magic-link tokens, and PINs grant access to sensitive portal records.

Mitigation: Use only your own authorized portal; restrict cookie-file permissions and keep credentials off shared machines, logs, shell history, and repositories.

Risk: Downloaded documents and command output may expose medical or billing information.

Mitigation: Handle PDFs and output as sensitive data; avoid storing or sharing them in unsecured locations.

## Reference(s):

- [SimplePractice FPX on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice-fpx)
- [SimplePractice Client Portal request reference](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal guidance; command results can contain sensitive medical and billing information.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
