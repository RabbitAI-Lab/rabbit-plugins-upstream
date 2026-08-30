## Description:

Looks up Zillow real-estate listings, property details, Zestimates, saved Zillow homes and searches, market reports, and mortgage calculations through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Zillow property searches, property records, saved Zillow activity, market reports, and mortgage-payment estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved Zillow homes and saved searches may be returned to the agent when the user asks for signed-in Zillow activity.

Mitigation: Use the skill only when the user is comfortable sharing saved Zillow activity with the active agent session.

Risk: The skill routes read-only Zillow requests through a signed-in browser session and unofficial Zillow endpoints, which may carry account or terms-of-use risk.

Mitigation: Install and use the skill only after reviewing the Zillow account and terms implications for this access pattern.

Risk: Captcha or sign-in state can interrupt saved-data and some Zillow data retrieval workflows.

Mitigation: Keep a signed-in Zillow browser tab available and resolve any captcha challenge directly in the browser before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source](https://github.com/chrischall/zillow-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zillow listing data, property details, saved homes or searches, market metrics, and mortgage breakdowns returned to the agent.]

## Skill Version(s):

0.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
