## Description:

Helps agents generate and edit images from text prompts and optional reference images using Nano Banana 2.0 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can create or edit images from prompts and reference images through dLazy's hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Confirm use of the hosted service before submitting prompts or media; avoid sharing sensitive content without authorization.

Risk: Authentication can save a dLazy API key locally.

Mitigation: Protect the local API key and rotate or revoke it if compromised.

Risk: Installing an external CLI package introduces supply-chain exposure.

Mitigation: Review the pinned CLI package before installation and prefer on-demand npx use when a global installation is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source (declared in skill metadata; release import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Image URLs, Guidance]

**Output Format:** [Markdown guidance and CLI JSON containing hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated images locally or return an asynchronous task identifier.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
