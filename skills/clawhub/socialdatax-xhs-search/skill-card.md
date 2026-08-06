## Description:

Searches Xiaohongshu, XHS, and RedNote notes through SocialDataX for keyword research, content analysis, competitor analysis, and trend scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to query XHS or RedNote notes by keyword via SocialDataX and summarize visible results for topic discovery, content planning, competitor research, market observation, and trend scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key and runs the SocialDataX npm package to perform searches.

Mitigation: Confirm trust in SocialDataX, install from the declared npm package, and provide the API key only through SOCIALDATAX_API_KEY.

Risk: Search results may include traceability URLs and pagination tokens that lose value if truncated, normalized, or rebuilt.

Mitigation: Preserve returned note URLs, note IDs, and pagination tokens exactly when displaying, storing, forwarding, or reusing them.

Risk: The skill fetches bounded search pages and may not represent complete platform coverage.

Mitigation: State the fetched scope in summaries and use page or recency limits that match the user's research request.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and API result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY; returned note URLs, note IDs, and pagination tokens should be preserved exactly when used.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
