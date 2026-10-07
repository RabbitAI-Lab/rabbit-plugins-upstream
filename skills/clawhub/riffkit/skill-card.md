## Description:

Helps create short-form AI videos and UGC-style ads from a video link, uploaded clip, or analyzed template, with optional characters, products, and language choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn a source video or template into a short-form promotional video or ad, then receive a video link and post-ready text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional heartbeat can overwrite local skill instructions with remote updates.

Mitigation: Disable automatic updates unless changes can be reviewed before installation.

Risk: The local account session token can grant access to the Riffkit account.

Mitigation: Protect or delete ~/.riffkit/session when not in use.

Risk: Video renders and retries may spend credits; uploads and account changes may expose or alter user data.

Mitigation: Confirm costs and file purpose before submissions or uploads, and require approval before retries, billing, or account changes.

## Reference(s):

- [Riffkit skill release](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill instructions](https://riffkit.ai/SKILL.md)
- [Riffkit API reference](https://riffkit.ai/skill/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a video link and post text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation may require account credits; the skill does not publish videos.]

## Skill Version(s):

1.9.3

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
