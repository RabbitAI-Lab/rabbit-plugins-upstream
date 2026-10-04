## Description:

Helps agents search and read public Groupon deals, deal details, and categories using terminal curl recipes without an account or API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users can find offers in a city, inspect a deal's prices and terms, and browse Groupon categories using public deal data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal searches are sent to Groupon's public endpoint; adding credentials or purchase workflows would change the security posture.

Mitigation: Do not add cookies, account tokens, or purchase actions without separately reviewing and trusting the authenticated integration.

Risk: Saved query fingerprints may expire, causing deal lookups to fail.

Mitigation: Check responses before relying on results and refresh stale fingerprints using the documented procedure.

## Reference(s):

- [Groupon curl recipes](references/graphql-queries.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/groupon-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with curl commands and deal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public deal reads; no account, cookies, or API key required.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
