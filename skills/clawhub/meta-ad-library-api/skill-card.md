## Description:

Search the Meta Ad Library by keyword or Facebook Page id and walk full cursor pagination through every ad, with creative, run dates, platforms and political spend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and research analysts use this skill to query Scavio's Meta Ad Library API for public Facebook and Instagram ad data, including advertiser pages, creative details, pagination, run dates, platform placement, and political ad disclosures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and lookup identifiers are sent to Scavio to perform Meta Ad Library searches.

Mitigation: Use the skill only when Scavio is an acceptable API provider for the user's data and workflow.

Risk: SCAVIO_API_KEY is required for API access.

Mitigation: Keep the key in an environment variable or secret store and do not place it in source code.

Risk: Deep cursor walks consume credits on each page.

Mitigation: Set a page cap and tell the user the expected credit budget before crawling.

Risk: Commercial Meta ads do not expose spend and reach fields, while political and issue ads may.

Mitigation: Do not interpret null spend or reach as zero; explain Meta's disclosure limits when reporting results.

## Reference(s):

- [Scavio Meta Ads documentation](https://scavio.dev/docs/meta-ads-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=meta-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=meta-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/meta-ad-library-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API requests, shell commands, and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume credits per page and return public logged-out ad data through Scavio.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
