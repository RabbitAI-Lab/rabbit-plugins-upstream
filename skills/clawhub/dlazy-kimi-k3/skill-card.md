## Description:

Moonshot AI thinking model with text, image, and video understanding for complex analysis, coding, and writing tasks that need long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke Kimi K3 through the dLazy CLI for complex reasoning, coding, writing, and multimodal analysis tasks with text prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded image or video files are sent to the dLazy cloud service for inference.

Mitigation: Avoid submitting sensitive prompts or local files unless dLazy is appropriate for that data.

Risk: The skill depends on the dLazy npm CLI and API credentials.

Mitigation: Review the linked source or package before installation, prefer per-invocation credentials where practical, and rotate or revoke API keys when needed.

Risk: The optional --save path writes generated results to the local filesystem.

Mitigation: Use explicit save paths and review the destination before running commands that persist outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [JSON envelope containing generated model output; asynchronous calls may return task status for polling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Optional image and video inputs may upload local files to dLazy-hosted media storage, and --save can write returned results to a local path.]

## Skill Version(s):

1.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
