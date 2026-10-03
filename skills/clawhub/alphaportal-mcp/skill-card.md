## Description:

Guides authorized users through accessing AlphaPortal student transportation records, live bus locations, and notifications with shell-based API calls instead of the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized AlphaPortal account holders and developers use this skill to retrieve student transportation data and, when needed, change notification preferences or walk-zone radius via direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracting and handling a browser refresh token can expose account access.

Mitigation: Use only with explicit account authorization; prefer approved workflows with scoped credentials and auditability, and do not share tokens.

Risk: API responses can expose student records and live bus locations.

Mitigation: Restrict access to authorized users and protect or avoid retaining sensitive responses.

Risk: Direct write calls can change real transportation settings without confirmation.

Mitigation: Prefer an approved workflow with a preview and confirmation gate; independently verify the target and intended change before any write.

## Reference(s):

- [AlphaPortal MCP release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)
- [AlphaPortal endpoint reference](artifact/references/endpoints.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell snippets and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may expose sensitive account and student data; write calls have no built-in confirmation.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
