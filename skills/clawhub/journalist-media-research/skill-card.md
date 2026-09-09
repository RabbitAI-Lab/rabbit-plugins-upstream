## Description:

Build a relevant journalist and media shortlist for a story or PR brief using Crawlora's journalists dataset, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External communications teams, PR practitioners, and agents use this skill to identify reporters whose actual coverage fits a story or PR brief, verify recent relevant work, and return a supported media shortlist. Pitch delivery remains a separate action requiring the user's request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can send the Crawlora API key and request data to an unintended host if CRAWLORA_API_BASE is controlled by untrusted configuration.

Mitigation: Run the skill only in a trusted environment, keep CRAWLORA_API_BASE unset or pinned to https://api.crawlora.net/api/v1, and review the helper before installing.

Risk: Media research prompts or request bodies may contain sensitive unpublished story or PR details.

Mitigation: Avoid passing secrets or sensitive unpublished research to Crawlora requests unless the user accepts that exposure.

Risk: Journalist contact data and beat labels may be incomplete, stale, or not evidence of pitch consent.

Mitigation: Verify current affiliation and recent bylined work on source pages, keep uncertain candidates labeled as unverified, and do not invent contact addresses from outlet patterns.

## Reference(s):

- [journalist-media-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/journalist-media-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown table or CSV with supporting evidence; shell commands may be included for Crawlora API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; the bundled helper prints raw JSON from Crawlora endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
