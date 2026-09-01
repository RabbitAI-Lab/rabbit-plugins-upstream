## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition, suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-detail Seedream 5.0 Pro images, including commercial key visuals, typography-sensitive compositions, and brand assets through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local image paths passed to the skill are sent to the third-party dLazy hosted API.

Mitigation: Treat prompts and image inputs as data disclosed to dLazy, and avoid sending sensitive content unless that use is acceptable.

Risk: The skill can store an organization API key in ~/.dlazy/config.json, and the security evidence says the inspected CLI code does not enforce the restricted file permissions claimed by the skill.

Mitigation: Prefer DLAZY_API_KEY for per-invocation use or check local config permissions after login; rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns generated image URLs from files.dlazy.com; with --save it can download the result asset locally, and async mode returns a generateId for polling.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
