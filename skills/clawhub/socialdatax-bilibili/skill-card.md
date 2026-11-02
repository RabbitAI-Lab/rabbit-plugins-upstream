## Description:

Search and analyze Bilibili videos, articles, comments, reactions, and creator profiles and posts, with optional video downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can research Bilibili content and creators by searching videos and articles, reviewing content details, comments and reactions, and retrieving creator profiles and posts. They can also save a video locally when they explicitly request a download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send supplied inputs to SocialDataX and may consume account credits.

Mitigation: Avoid confidential text and token-bearing URLs; check the expected query scope and available credits before running requests.

Risk: The CLI is installed through npm, and examples use the latest package version.

Mitigation: Pin a reviewed package version instead of using @latest.

Risk: Optional video downloads write files locally and require ffmpeg.

Mitigation: Choose the intended output directory and ensure ffmpeg is available before downloading.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [Structured data and concise text summaries; optional downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video downloads are optional and save files to a user-selected local directory.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
