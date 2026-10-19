## Description:

Guides agents in creating short AI videos and UGC-style ads from source videos or an original creative direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use the skill to direct short-form videos and product ads, either by adapting a source video's emotional arc, swapping its subjects, or supplying an original brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic updates can replace local skill instructions with content from Riffkit's server.

Mitigation: Install only if you trust Riffkit to update the skill; disable the heartbeat updater or review updates before use.

Risk: A locally stored account session token can grant access to the Riffkit account.

Mitigation: Protect ~/.riffkit/session as an account credential.

Risk: Someone holding an upload or video link can use it during its validity window.

Mitigation: Share upload and video links only with intended recipients.

Risk: Video requests, retries, cancellations, or plan actions can affect credits or account state.

Mitigation: Confirm the quoted price and each credit-spending, retry, cancellation, or plan action with the user before proceeding.

## Reference(s):

- [Riffkit on ClawHub](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit](https://riffkit.ai)
- [Riffkit skill documentation](https://riffkit.ai/SKILL.md)
- [Riffkit API reference](https://riffkit.ai/skill/api.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Video links]

**Output Format:** [Plain text with CLI commands, quoted prices, and links to completed videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video links are shared only after a finished task returns an asset ID.]

## Skill Version(s):

1.10.4 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
