## Description:

This skill helps social media operators monitor TikTok topics, video rankings, keyword search results, video details, and comments so they can turn trend evidence into content ideas and calendars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators and content teams use this skill to research TikTok trends, competitor activity, audience comments, and high-engagement videos before planning short-form video topics. It is intended to produce actionable topic lists, hot-topic summaries, competitor-account updates, and concise audience-insight notes rather than raw data dumps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Qinghu API token.

Mitigation: Request only the Qinghu token needed for the task, prefer environment variables when available, and avoid exposing token values in responses or exports.

Risk: The skill may call paid Qinghu external APIs.

Mitigation: Obtain user confirmation before the first API call in a session, disclose that calls may consume Qinghu points, and report actual point consumption when returned by the API envelope.

Risk: The skill may create local export files for larger TikTok datasets.

Mitigation: Export only task-relevant records, provide concise previews instead of pasting large datasets into chat, and direct the user to generated files when exports are created.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-social)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, API calls, guidance]

**Output Format:** [Markdown responses with concise summaries, optional exported table files, and Qinghu API call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export larger TikTok result sets locally and should report Qinghu point consumption after paid calls.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
