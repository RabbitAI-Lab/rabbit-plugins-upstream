## Description:

Helps users turn a TikTok video, uploaded clip, analyzed template, or original idea into a short-form AI video or product ad.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and other users use the skill to plan and request short-form AI videos and UGC-style ads from a source clip, template, or original idea, then review the result before posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended remote updates can replace local skill instructions.

Mitigation: Review the heartbeat and update setup before installation; disable unattended updates unless future changes from riffkit.ai are trusted.

Risk: A local Riffkit session grants access to the user's account.

Mitigation: Treat ~/.riffkit/session as a live credential; never share it or include it in prompts or uploads.

Risk: Uploading a local file may disclose content the user did not intend to share.

Mitigation: Confirm the file and its purpose before uploading it to Riffkit.

Risk: Video generation and retries may incur credit charges.

Mitigation: Confirm quoted credit costs before submitting and request approval before retrying failed tasks.

## Reference(s):

- [Riffkit skill release](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit homepage](https://riffkit.ai)
- [Riffkit API reference](https://riffkit.ai/skill/api.md)
- [Riffkit installation guide](https://riffkit.ai/skill/install.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a video link and post text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include creative plans, price quotes, and approval prompts before a paid request.]

## Skill Version(s):

1.10.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
