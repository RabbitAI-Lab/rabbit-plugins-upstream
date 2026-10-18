## Description:

Guides an agent to generate a short video from a first-frame image and prompt using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents use this skill to request a short video from a supplied first-frame image and text prompt, and retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI and invoking a hosted service introduces software and service trust dependencies.

Mitigation: Review the pinned dLazy CLI package and linked source before installation and use.

Risk: Submitted images and prompts may be uploaded to dLazy, and the CLI stores or uses an API key.

Mitigation: Avoid sending sensitive media without authorization; protect the API key and rotate or revoke it if exposed.

Risk: Example image flag and media output format differ from the documented first-frame option and video purpose.

Mitigation: Confirm the live CLI help for the first-frame flag and inspect the actual output before relying on the examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text with CLI commands; CLI results are JSON with generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a first-frame image and prompt; generated media can be downloaded locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
