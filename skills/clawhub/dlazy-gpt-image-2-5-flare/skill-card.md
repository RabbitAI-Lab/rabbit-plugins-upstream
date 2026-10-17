## Description:

Generates and edits images from text prompts and optional reference images through dLazy's hosted GPT Image 2.5 Flare service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and reference images via the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, which also hosts generated outputs.

Mitigation: Avoid submitting sensitive prompts or media unless sharing them with dLazy is acceptable.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the documented npx invocation if a persistent global installation is not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image files]

**Output Format:** [JSON response with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an image URL.]

## Skill Version(s):

1.2.19 (source: server release metadata; bundled skill frontmatter and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
