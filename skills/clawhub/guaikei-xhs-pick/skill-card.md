## Description:

Searches Xiaohongshu public notes, retrieves note details and comments, and fetches creator post lists as structured data for content research, competitor analysis, KOL screening, and trend discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, marketers, and analysts use this skill to collect public Xiaohongshu search, note, comment, and creator-post data before performing downstream summaries, reports, or market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu note or profile links, and the GUAIKEI_API_TOKEN are sent to the third-party guaikei.com service.

Mitigation: Use the skill only when third-party API processing is acceptable, scope the token appropriately, and avoid submitting sensitive business research unless approved.

Risk: Fetched public content and search results may persist in the local logs directory.

Mitigation: Review and clean the logs directory after use when results contain sensitive research topics or should not remain on the machine.

Risk: The skill is limited to public Xiaohongshu data and should not be used for private, hidden, or login-gated content.

Mitigation: Keep use cases to public-data retrieval and verify that downstream use complies with platform rules and internal data policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-pick)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON results with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes fetched results to a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
