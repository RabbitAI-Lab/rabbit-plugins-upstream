## Description:

Riffkit helps an agent turn one source, such as a TikTok link, uploaded video, or analyzed template, into a post-ready short-form AI video or UGC-style ad creative with optional character, product placement, language, and creative direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use Riffkit to draft, submit, monitor, and deliver short AI videos based on an existing source video's emotional formula or an original creative direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat update path can overwrite the installed skill from a mutable remote file that does not currently match the submitted artifact.

Mitigation: Disable automatic heartbeat updates or review downloaded SKILL.md changes before use.

Risk: The skill uses a vee_session authentication cookie and can perform cost-sensitive generation, retry, product upload, and subtitle-editing actions.

Mitigation: Protect the vee_session like a password and require explicit user confirmation before cost-sensitive or persistent actions.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [ClawHub skill listing](https://clawhub.ai/riffkit/skills/riffkit)
- [ClawHub publisher profile](https://clawhub.ai/user/riffkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API calls, shell commands, configuration snippets, status summaries, video links, captions, hashtags, and strategy recap text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces agent-facing guidance and commands for using the Riffkit service; it requires explicit user confirmation before cost-sensitive generation, retry, product upload, or subtitle-editing actions.]

## Skill Version(s):

1.2.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
