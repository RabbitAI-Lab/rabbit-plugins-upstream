## Description:

Turns product specs, catalogs, manuals, or marketplace listings into conversion-focused ecommerce videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce teams use this skill to create product advertising and cross-border selling videos from product descriptions, documents, or marketplace listings. Developers and agents use it through the pinned dLazy CLI workflow to start or continue project-scoped video generation sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product details, and explicitly attached files may be sent to dLazy services during use.

Mitigation: Use only product data and files approved for dLazy processing, and avoid attaching sensitive materials unless that transfer is acceptable.

Risk: The dLazy API key can consume organization credits if exposed or misused.

Mitigation: Treat the API key as a credential, store it securely, and rotate or revoke it from the dLazy dashboard when needed.

Risk: The workflow depends on a pinned third-party npm CLI package.

Mitigation: Review the pinned package and source repository before installation when supply-chain trust is a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown-style text with CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project-session guidance, authentication guidance, and references to uploaded files handled through the dLazy CLI.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
