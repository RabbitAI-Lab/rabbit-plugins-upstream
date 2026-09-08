## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images. Suited to key visuals, posters and anything meant for large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate high-resolution Doubao Seedream images from text prompts and optional reference images for visual design, posters, and print-oriented creative work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the pinned third-party CLI introduces supply-chain and local execution risk.

Mitigation: Review the @dlazy/cli package before installing and prefer npx or a non-privileged isolated environment when a persistent global CLI is not needed.

Risk: API keys saved in the local CLI configuration could be exposed if the machine or config file is compromised.

Mitigation: Store keys only on trusted systems and rotate or revoke the dLazy API key if the machine or config file may have been exposed.

Risk: Local media paths passed to the skill are uploaded to dLazy media storage for model processing.

Mitigation: Only pass local files that the user intends to upload to dLazy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated image URLs or asynchronous task status.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
