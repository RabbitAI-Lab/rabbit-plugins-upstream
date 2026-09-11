## Description:

Enables agents to query Redfin through the fpx CLI for location resolution, listing search, property details, market trends, rentals, climate risk, photos, and signed-in saved-home or saved-search data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when they need Redfin real-estate data from shell workflows without running the redfin MCP server. It supports scripted lookups for listings, property details, market context, and account-specific saved items when the browser session is signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent browser bridge that can access a signed-in Redfin session, including saved homes and saved searches.

Mitigation: Use a dedicated browser profile when possible, keep Redfin site access narrowly scoped, avoid signing in unless saved items are needed, and revoke fpx pairing or extension access when finished.

Risk: Installing the fpx CLI globally without pinning can introduce supply-chain control gaps in stricter environments.

Mitigation: Pin and verify the @fetchproxy/cli package when your environment requires stronger supply-chain controls.

Risk: Redfin responses can be rejected or can substitute a nearby indexed region, which may make returned listing data unreliable.

Mitigation: Strip the anti-CSRF prefix, verify resultCode is 0, and compare serviceRegionName and listing locations against the requested region before relying on results.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include fpx CLI commands and JSON parsing guidance; users should check Redfin result envelopes before trusting payloads.]

## Skill Version(s):

0.13.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
