## Description:

Given a company name or ticker, this skill produces a concise five-section A-share briefing with anchored company facts, four-period financials, dated events, directly checked risks, and an opinion section left blank for human completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and client-facing professionals can use this skill for a quick, source-anchored introduction to a company before a meeting. It is not for investment advice or in-depth due diligence, and its opinion section is reserved for human completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passing checker may not catch gaps that could make a company briefing inaccurate or misleading.

Mitigation: Review the report against its original disclosures, including the opinion section; do not treat a passing checker as sufficient.

Risk: A Cue API key could be exposed if sent to an untrusted destination or included in chat.

Mitigation: Verify the destination is a trusted HTTPS endpoint before sending the key, and keep the key out of chat; user-supplied disclosures are an alternative when not enabling Cue.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-tear-sheet)
- [Cue API key guide](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown company briefing with five fixed sections, source-index records, and a separate run log]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to five companies per request; missing data is omitted rather than estimated, and the opinion section remains blank for human completion.]

## Skill Version(s):

0.1.19 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
