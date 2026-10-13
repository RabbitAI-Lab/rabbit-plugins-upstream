## Description:

Helps turn presentations and other documents into narrated explainer, training, or pitch videos through dLazy's hosted file-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to turn presentations or documents into narrated video explainers, courseware, pitches, and training material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to an external service.

Mitigation: Share only content you are authorized to upload and review attachments before sending.

Risk: The CLI may store an API key locally.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: A global npm installation persists, and broad trigger phrases can invoke this skill unexpectedly.

Mitigation: Prefer the pinned on-demand npx invocation if persistence is unwanted; confirm the user's intent before invoking the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation takes place through the dLazy service.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
