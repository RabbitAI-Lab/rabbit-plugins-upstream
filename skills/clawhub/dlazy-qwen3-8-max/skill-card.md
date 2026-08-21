## Description:

Alibaba's flagship Qwen reasoning model for complex reasoning, code engineering, long-context analysis, and text or image-assisted generation through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to invoke Qwen 3.8 Max for reasoning, coding, long-context analysis, and multimodal text or image-assisted generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files explicitly passed to the skill are sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive data unless that use is approved, and pass local media files only when upload to the hosted service is intended.

Risk: Using login or auth set stores a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation credentials when persistence is not desired, protect the local config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy package on the host.

Mitigation: Use the pinned npx invocation when a persistent global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON CLI response containing generated model outputs; agent-facing content may be text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy API authentication. Local media paths supplied as inputs may be uploaded to dLazy media storage.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
