## Description:

Turns a YouTube video into a Chinese conversational podcast using NotebookLM, then uploads it to Xiaoyuzhou as a draft by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seuwangcy](https://clawhub.ai/user/seuwangcy)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw agents use this skill when a user shares a YouTube link and wants a Chinese podcast version prepared for a Xiaoyuzhou show. It saves a draft by default and reports the result in the originating conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security scan marks the release suspicious, citing link-triggered podcast processing and ClawHub publishing instructions outside the main workflow.

Mitigation: Review the trigger and setup actions before enabling the skill, including its environment, file, network, and shell access.

Risk: Public episode publishing is irreversible.

Mitigation: Keep draft mode as the default and publish only when explicitly requested, with both required authorization flags set.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/seuwangcy/skills/yt2podcast)
- [OpenClaw documentation](https://docs.openclaw.ai)
- [opencli package](https://www.npmjs.com/package/@jackwener/opencli)
- [Xiaoyuzhou](https://www.xiaoyuzhoufm.com/)

## Skill Output:

**Output Type(s):** [Audio, Text]

**Output Format:** [Podcast audio (M4A when conversion succeeds) and a Chinese completion message with the episode link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft by default; public publishing requires both --publish and YT2PODCAST_ALLOW_PUBLISH=1.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence and CHANGELOG.md, released 2026-11-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
