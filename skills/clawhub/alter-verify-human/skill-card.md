## Description:

Use when an agent needs to confirm a specific person is a known, verified identity before transacting with them, granting access, accepting a claim about their credentials, or relaying a decision on their behalf.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to verify that a named person is registered or verified on ~alter before granting access, accepting credential claims, completing transactions, or relaying a consequential decision. It supports checks by handle, member ID, or email, and can evaluate verification tier, archetype, and trait-range claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends person identifiers and claim checks to ~alter's hosted MCP service.

Mitigation: Use it only for a specific person when verification is relevant to a decision, and avoid broad or speculative email lookups.

Risk: The skill requires an ALTER_API_KEY credential.

Mitigation: Treat the key as a credential, store it securely, and never paste or fabricate keys in conversation.

Risk: Engagement level can be misused as an access or trust score.

Mitigation: Do not gate transactions, access grants, or services on engagement level; use verification tier or specific trait-range checks for relevant claims.

## Reference(s):

- [~alter MCP endpoint](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-verify-human)
- [Publisher profile](https://clawhub.ai/user/true-alter)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance with JSON MCP tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ALTER_API_KEY credential for calls to the hosted ~alter MCP service.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
