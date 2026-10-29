## Description:

Adapts web novels into webtoon episode breakdowns and scripts, with guidance for visual pacing and continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External writers and adaptation teams can use the skill to turn a web novel into tagged episode beats and visual, cliffhanger-driven webtoon scripts in Chinese.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied workflow may steer writing requests into cloud image generation even when image generation was not requested.

Mitigation: Keep image generation optional and limited to image requests; review the content sent to dLazy and any charges before confirming.

Risk: Logging in stores the service key in the local CLI configuration.

Mitigation: Protect the local configuration, or use the documented environment variable for per-run credentials; rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese text and Markdown episode breakdowns and scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversation-based input; episode scripts follow a setup, escalation, turn, and hook structure.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
