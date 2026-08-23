## Description:

Searches public Douyin content, creator posts, video comments, and trending topics through CLI commands for content research, competitor analysis, sentiment insight, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect public Douyin search results, creator posts, comments, and hot-list data for short-video planning, competitor monitoring, comment sentiment review, and trend tracking. It is not intended for publishing videos, downloading watermarked content, or accessing private Douyin data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broad auto-activation rules, including use for content research even when Douyin is not explicitly named.

Mitigation: For ambiguous short-video or content-research requests, confirm that the user wants Douyin before running the skill.

Risk: The security review notes that Douyin keywords, target URLs, request parameters, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install and run only after reviewing the data-sharing and token requirements; avoid sending sensitive search terms or target URLs.

Risk: Successful search, post, and comment results may be saved under the local logs directory.

Mitigation: Review, retain, or delete generated logs according to the user's data-handling requirements.

Risk: The security review reports contradictory runtime token/contact behavior.

Mitigation: Before deployment, verify that authentication failures produce neutral guidance and do not expose unwanted contact or marketing text.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-comments-for-sentiment-insight)
- [Usage Guide and FAQ](readme.md)
- [Complete CLI Options](references/options.md)
- [Changelog](references/changelog.md)
- [CLI Request and Response Schemas](assets/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI stdout is structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful CLI results may be saved under a local logs directory.]

## Skill Version(s):

1.0.0 (source: release metadata, package.json, changelog, and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
