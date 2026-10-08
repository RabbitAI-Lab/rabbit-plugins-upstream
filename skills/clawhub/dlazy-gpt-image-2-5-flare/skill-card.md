## Description:

Guides text-to-image generation and image editing with the dLazy GPT Image 2.5 Flare CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy-hosted services.

Mitigation: Confirm you trust the dLazy service before submitting sensitive prompts or media.

Risk: The dLazy CLI stores an API key locally and a global install persists on the system.

Mitigation: Protect the local key, rotate or revoke it through the dLazy dashboard when needed, and use npx if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with generated image URLs or an asynchronous task ID; images can be saved locally.]

## Skill Version(s):

1.2.15 (source: ClawHub release evidence; CLI install spec pins 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
