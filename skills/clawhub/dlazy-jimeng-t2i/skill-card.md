## Description:

Helps agents generate images from text prompts using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to ask an agent for Jimeng-generated images from text prompts, optionally with reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected files are sent to dLazy's cloud service.

Mitigation: Avoid submitting private prompts or local files unless you are comfortable sharing them with dLazy.

Risk: Authentication uses a dLazy API key stored in local CLI configuration.

Mitigation: Keep the key private and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON responses, Image URLs]

**Output Format:** [Markdown guidance and CLI JSON responses linking to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can optionally be saved locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
