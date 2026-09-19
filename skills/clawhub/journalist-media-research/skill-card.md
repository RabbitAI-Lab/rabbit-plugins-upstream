## Description:

Build a relevant journalist and media shortlist for a story or PR brief using Crawlora's journalists dataset, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, communications teams, and agents use this skill to find journalists whose beats and recent published work match a story or PR brief. It helps produce a verified media shortlist with supporting article evidence and public contact-source details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and the research queries or URLs submitted through this skill.

Mitigation: Use the skill for public journalist and media research, keep the API key in a private environment variable, and avoid storing it in shared shell profiles or logs.

Risk: Journalist affiliations, coverage history, and public contact details may be stale or incomplete.

Mitigation: Verify current affiliation, bylines, article dates, and contact-source URLs before outreach, and mark uncertain candidates as unverified.

Risk: The curated journalist dataset can omit relevant reporters or outlets.

Mitigation: Supplement empty or narrow dataset results with public search and explain any shortfall against the requested list size.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/journalist-media-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown table or CSV with supporting links, article dates, contact-source URLs, retrieval dates, and verification status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shell commands for Crawlora API calls and should explain shortfalls or unverified candidates.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
