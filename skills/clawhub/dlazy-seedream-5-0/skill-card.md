## Description:

Helps agents generate 2K, 3K, or 4K images from prompts and reference images using dLazy's Seedream 5.0 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating high-resolution visuals, posters, and print-ready artwork from text prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key is stored locally for authenticated requests.

Mitigation: Protect local credentials and rotate or revoke the key if needed.

Risk: Prompts and selected reference images are sent to dLazy cloud endpoints.

Mitigation: Send only content you are comfortable sharing with dLazy.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the documented npx option for on-demand execution if a global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands; CLI responses are JSON containing image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K generation; results can be saved locally.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
