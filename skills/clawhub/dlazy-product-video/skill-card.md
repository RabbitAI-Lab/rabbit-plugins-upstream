## Description:

Turns product photos, specifications, or store listings into product demo and advertising videos using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and sellers use this skill to create product demonstrations and ecommerce ads from product images, documents, or listing links, with multilingual voiceover and an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product details, and attached files may be sent to dLazy's hosted service.

Mitigation: Avoid uploading secrets or private documents unless intended, and review files before attaching them.

Risk: The CLI stores a dLazy API key in local configuration.

Mitigation: Protect the local configuration and rotate or revoke the key when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI repository (skill metadata link; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service generates product videos; agent responses may include project status and results.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
