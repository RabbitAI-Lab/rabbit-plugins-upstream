## Description:

Retrieves basic Douyin account information and up to 50 recent works for a supplied Douyin nickname or ID, including engagement metrics, direct links, and top-engagement highlights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, MCN operators, creators, and data analysts use this skill to review recent Douyin account performance, compare competitor or creator content, and export structured account and works data for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send Douyin account names or IDs to the RedFox API.

Mitigation: Use only approved targets, avoid sensitive or regulated accounts, and prefer precise Douyin IDs to reduce unintended lookups.

Risk: The command output prints the first characters of REDFOX_API_KEY.

Mitigation: Remove or patch API-key-prefix logging before using this skill in shared terminals, CI logs, or agent transcripts.

Risk: Nickname queries can return a fuzzy match for the wrong Douyin account.

Mitigation: Prefer Douyin IDs for precision and confirm the returned nickname before relying on the report.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/redfox-data/skills/douyin-works-crawler)
- [Core workflow reference](references/core_workflow.md)
- [RedFox API endpoint](https://redfox.hk/story/api/dyData/queryUserWithWorks)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report by default; optional JSON from the script's --output json mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; returns recent works only, up to 50 items, ordered reverse chronologically.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
