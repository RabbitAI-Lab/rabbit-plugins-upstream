## Description:

Build a relevant journalist and media shortlist for a story or PR brief using Crawlora's journalists dataset, news search, and public author pages. Use to find reporters by beat or outlet, verify recent coverage, and collect published work contact channels with supporting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External communications, PR, and media relations users use this skill to build a researched shortlist of reporters whose recent coverage matches a story brief. The agent verifies fit with public author pages, news search, and cited article evidence before returning media-list rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends journalist queries, search terms, and target URLs to the external Crawlora service.

Mitigation: Avoid submitting confidential briefs or sensitive target URLs unless the intended use allows disclosure to Crawlora.

Risk: The workflow requires a Crawlora API key.

Mitigation: Keep the API key in the environment, do not paste it into prompts or files, and rotate it if exposure is suspected.

Risk: Dataset labels and public snippets can be stale or incomplete for journalist affiliation and recent coverage.

Mitigation: Verify current affiliation, bylines, article dates, and contact source pages before using the shortlist.

## Reference(s):

- [journalist-media-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/journalist-media-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown table or CSV with cited URLs and verification status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes reporter identity, outlet, beat, profile URL, relevant article URLs and dates, fit reason, public contact, contact source URL, retrieval date, and verification status.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
