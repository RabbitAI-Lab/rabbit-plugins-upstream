## Description:

Search the Meta Ad Library by keyword or Facebook Page id and walk full cursor pagination through every ad, with creative, run dates, platforms and political spend. 3 endpoints, 1 credit per page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and analysts use this skill to retrieve public Meta Ad Library data for competitor research, creative review, advertiser monitoring, and political or issue ad analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and Facebook Page IDs are sent to Scavio.

Mitigation: Use the skill only for appropriate public ad-library queries and avoid submitting sensitive internal campaign plans or private identifiers.

Risk: Broad pagination can consume paid API credits.

Mitigation: Set a page or credit budget before crawling and stop when the planned cap is reached.

Risk: API keys can be exposed if copied into source files or shared logs.

Mitigation: Use a dedicated Scavio API key, load it from the environment or a secret store, and keep it out of source control.

Risk: Meta reports capped totals and omits commercial spend data, which can lead to misleading conclusions.

Mitigation: Present capped totals as capped, do not treat null spend or reach as zero, and distinguish political or issue ad disclosures from commercial ad data.

Risk: Ad creative may be copyrighted by third parties.

Mitigation: Quote creative only for analysis and do not present retrieved creative as original user-owned material.

## Reference(s):

- [Scavio Meta Ads documentation](https://scavio.dev/docs/meta-ads-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-meta-ads)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, API calls, JSON]

**Output Format:** [Markdown guidance with JSON request and response details plus Python and JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to call Scavio's Meta Ads API; API responses are structured JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
