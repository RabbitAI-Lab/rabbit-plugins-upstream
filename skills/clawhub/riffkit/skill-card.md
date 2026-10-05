## Description:

Creates short AI videos and UGC-style ads by adapting a source video's creative formula, swapping elements in its shots, or generating a video from a written idea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to make short-form videos or product ads from a source video, an uploaded clip, a template, or a written idea, then receive a video link and post text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic updates can replace installed skill instructions without independent integrity verification.

Mitigation: Disable the automatic heartbeat or review each update manually until signed hashes or another integrity check is available; install only if you trust Riffkit's future updates.

Risk: The local Riffkit session grants access to the user's account.

Mitigation: Treat ~/.riffkit/session as a sensitive credential; never paste or include its contents in prompts, task descriptions, or shared output.

Risk: Selected media, product details, creative prompts, and account metadata are sent to Riffkit.

Mitigation: Confirm the purpose of uploads and avoid submitting sensitive material unless the user intends to share it with Riffkit.

Risk: Video generation and retries can spend account credits.

Mitigation: Show the quoted price and obtain user approval before each paid render or retry.

## Reference(s):

- [Riffkit on ClawHub](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit homepage](https://riffkit.ai)
- [Riffkit API reference](https://riffkit.ai/skill/api.md)
- [Riffkit installation and updates](https://riffkit.ai/skill/install.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a generated video link and post text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video rendering may consume credits after the user approves a quoted price.]

## Skill Version(s):

1.9.2 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
