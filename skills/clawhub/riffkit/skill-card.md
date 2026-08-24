## Description:

Riffkit helps an agent create short AI videos from a TikTok link, uploaded video, analyzed template, or written creative direction, with optional character, product placement, language, and creative-direction settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to plan, submit, monitor, and deliver short-form riff videos or UGC-style ad creative through Riffkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat can automatically replace local skill instructions from the network without user approval or integrity checks.

Mitigation: Disable the heartbeat or review each SKILL.md update before replacement.

Risk: The Riffkit session token grants account access for API calls.

Mitigation: Treat the vee_session token like a login credential and avoid exposing it in logs, prompts, or shared files.

Risk: Generation, retry, upload, and product-write operations can affect paid usage or account state.

Mitigation: Require explicit user confirmation before paid generation, retry, upload, or product creation.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill source](https://riffkit.ai/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [ClawHub publisher profile](https://clawhub.ai/user/riffkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API paths, shell commands, request parameters, confirmation prompts, status handling, and delivery text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow guidance for authenticated Riffkit video generation and update checks.]

## Skill Version(s):

1.4.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
