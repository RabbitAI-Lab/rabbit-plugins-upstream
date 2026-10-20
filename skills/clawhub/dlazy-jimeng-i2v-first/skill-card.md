## Description:

Guides an agent to generate short Jimeng videos from a first-frame image and a text prompt using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to turn a supplied first-frame image and prompt into a short generated video through dLazy's Jimeng service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image files may be uploaded to dLazy, and generated media is hosted by dLazy.

Mitigation: Avoid sensitive images or prompts unless you are comfortable sharing them with the third-party service.

Risk: Login can save a dLazy API key in local configuration.

Mitigation: Protect the local account and rotate or revoke the key if it is exposed.

Risk: Running the third-party CLI requires trusting its installed code.

Mitigation: Review the pinned CLI source before use; use the pinned npx invocation if a global install is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return a hosted media URL or an asynchronous task ID; the generated asset can optionally be saved locally.]

## Skill Version(s):

1.3.32 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
