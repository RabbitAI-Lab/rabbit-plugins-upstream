## Description:

Helps agents generate images with Qwen Image 2 Pro through the dLazy CLI, including designs with complex text and mixed Chinese-English layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to request generated images from text prompts, optionally providing reference images and saving the results locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Review prompts and reference files before submission; avoid sending sensitive content unless its cloud processing is acceptable.

Risk: Login can store a dLazy API key in local configuration.

Mitigation: Protect the local account and rotate or revoke the key from the dLazy dashboard if needed.

Risk: Installing the CLI globally leaves a persistent executable on the system.

Mitigation: Prefer the pinned npx @dlazy/cli@1.2.3 invocation when a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source code](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs; optional local download and asynchronous task polling are supported.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
