## Description:

Helps an agent generate or edit images with Nano Banana 2 using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request new images or edits to reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files are sent to dLazy, and generated outputs are hosted by dLazy.

Mitigation: Use only for intentional image tasks and avoid submitting sensitive prompts or files unless appropriate for the dLazy service.

Risk: Logging in saves a dLazy API key locally.

Mitigation: Protect the local account and manage or revoke the key through dLazy when needed.

Risk: A global CLI installation persists on the machine.

Mitigation: Prefer the pinned npx @dlazy/cli@1.2.3 invocation when a persistent install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI homepage (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown guidance and commands; CLI results include JSON image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally on request.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
