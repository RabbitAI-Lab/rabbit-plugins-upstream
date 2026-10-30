## Description:

Scans a company's penalties and regulatory measures, external-guarantee proxy data, and (when applicable) global sanctions enforcement to produce a source-linked card that names unreached areas without assigning an overall risk score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can prepare a traceable company scan from a company name or six-digit code, with dated, sourced findings for reachable areas and explicit disclosures for areas not reached. It does not provide an overall risk rating, default probability, litigation or ownership-chain inference, or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-bearing connections could expose the Cue API key to an unapproved destination or unsafe redirect.

Mitigation: Use the manual/offline workflow until both credential-bearing paths enforce approved HTTPS destinations and safe redirect handling; avoid running the unchanged README POST with a live key.

Risk: Online lookups disclose company names or codes to Cue and may incur costs.

Mitigation: Approve the data sharing and costs before online searches.

Risk: Optional installation sources may introduce unreviewed code or content.

Mitigation: Review and pin optional installation sources.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-event-risk-scan)
- [Cue service](https://cuecue.cn)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown company scan card with source links and dated findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One company per card; distinguishes proxy data and unreached areas; does not assign an overall risk score.]

## Skill Version(s):

0.2.22 (source: SKILL.md frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
