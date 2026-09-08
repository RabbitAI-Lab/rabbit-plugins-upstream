## Description:

Access historical OpenMandate mandates, matches, and contacts or close retained work for an existing account with an existing API key while new mandates and integrations remain unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rsh3khar](https://clawhub.ai/user/rsh3khar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access retained OpenMandate records for an existing account and perform limited withdrawal actions such as closing a mandate, declining a match, or deleting a contact. It is intended only for users who already have an OpenMandate API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives agents command authority to close mandates, decline matches, and delete contacts.

Mitigation: Require the agent to show the exact mandate, match, or contact first and confirm the specific ID before taking any withdrawal action.

Risk: The OpenMandate API key grants access to account records and authorized retained actions.

Mitigation: Install only for an existing OpenMandate account whose API key the user is comfortable giving to this skill.

Risk: OPENMANDATE_BASE_URL can redirect requests away from the default OpenMandate API.

Mitigation: Do not set OPENMANDATE_BASE_URL to an untrusted endpoint.

## Reference(s):

- [OpenMandate retained-access API reference](references/api-reference.md)
- [OpenMandate homepage](https://openmandate.ai)
- [Hosted OpenMandate MCP endpoint](https://mcp.openmandate.ai/mcp)
- [OpenMandate API base URL](https://api.openmandate.ai)
- [ClawHub skill page](https://clawhub.ai/rsh3khar/skills/openmandate)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPENMANDATE_API_KEY; OPENMANDATE_BASE_URL may override the default API endpoint.]

## Skill Version(s):

0.6.2 (source: release evidence, artifact frontmatter, and helper script)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
