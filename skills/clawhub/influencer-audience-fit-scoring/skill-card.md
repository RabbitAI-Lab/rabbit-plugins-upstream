## Description:

Audience-fit analysis for pre-campaign decisions across YouTube, TikTok, and Instagram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creator-economy analysts, and agent users use this skill to evaluate whether a creator's audience matches a campaign ICP. It compares YouTube, TikTok, and Instagram audience dimensions and returns fit scores, confidence, score breakdowns, and go/test/no-go recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator identifiers and audience-analysis requests are sent to the configured Scrumball/SCData API gateway.

Mitigation: Use a trusted HTTPS SCRUMBALL_BASE_URL and a narrowly scoped environment file containing only SCRUMBALL settings.

Risk: Returned demographic and behavioral analytics may be privacy-sensitive campaign data.

Mitigation: Treat returned audience analytics as sensitive, limit sharing, and review fit recommendations before using them in campaign decisions.

Risk: A vague target ICP or missing audience dimension can make the fit score less reliable.

Mitigation: Ask for missing ICP details before scoring when needed, continue with lowered confidence when a dimension is unavailable, and show the dimension-by-dimension breakdown.

## Reference(s):

- [API Index](artifact/references/api-index.md)
- [Request and Response Guide](artifact/references/request-response.md)
- [Operations Manifest](artifact/references/operations.json)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with score summaries, JSON-backed API results, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns fit score, confidence, dimension breakdown, decision, and next validation action; prompts for missing ICP fields and lowers confidence when one dimension is unavailable.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
