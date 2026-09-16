## Description:

Access AlphaPortal school-bus data from shell workflows using refresh-token based authentication, direct REST API calls, and curl examples for students, stops, vehicle location, notifications, and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with authorized AlphaPortal access use this skill to retrieve school transportation records and live bus location data from scripts or machines where the MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles a reusable browser refresh token that is equivalent to account access.

Mitigation: Use only with authorized AlphaPortal accounts, keep tokens out of shared shells and logs, and rotate or recapture tokens when access should end.

Risk: The skill can expose sensitive student transportation records and live location data.

Mitigation: Limit use to authorized student records and environments approved for handling that data.

Risk: Some write examples change real transportation settings without the MCP server's dry-run confirmation.

Mitigation: Require separate confirmation and a rollback plan before running write examples.

Risk: The optional fpx browser bridge introduces additional dependency and pairing trust assumptions.

Mitigation: Avoid the bridge unless it has been independently reviewed and pinned.

## Reference(s):

- [AlphaPortal endpoint reference](artifact/references/endpoints.md)
- [AlphaPortal API base URL](https://api.alpharoute.app)
- [AlphaPortal refresh-token endpoint](https://api.alpharoute.app/AlphaCore/v1/public/refresh-token)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, JavaScript, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes authenticated read calls and examples for write endpoints that change transportation records.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
