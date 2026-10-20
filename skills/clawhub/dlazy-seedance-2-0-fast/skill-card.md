## Description:

Guides agents in generating short videos from prompts, media references, or first and last frames using dLazy's Seedance 2.0 Fast service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to ask an agent to generate short videos from text prompts and optional image, video, audio, or frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images, videos, or audio may be uploaded to dLazy's hosted service.

Mitigation: Only submit media you are comfortable sharing with the provider.

Risk: Login may save an API key to the local user configuration, and a global CLI installation persists.

Mitigation: Use the documented npx option for non-persistent CLI use; rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source (linked in skill metadata; not verified as skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns generated media links or an asynchronous task ID; the agent may explain how to save the result.]

## Skill Version(s):

1.3.31 (source: ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
