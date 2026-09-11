## Description:

Turns product specs, manuals, catalogs, or ecommerce listings into conversion-focused shopping videos with multilingual voiceover and an optional virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create product ads and cross-border ecommerce videos from product files or marketplace links. The skill delegates generation to the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external npm package and hosted dLazy service.

Mitigation: Use npx or an isolated environment, avoid running npm as root, and review the referenced source or package before use.

Risk: Attached local files are uploaded to dLazy media storage for processing.

Mitigation: Attach only files that are appropriate to share with dLazy and avoid sensitive product or customer data unless the user's organization has approved that use.

Risk: API keys are required for the dLazy service.

Mitigation: Use the documented login or auth setup, store keys in the CLI config or environment as intended, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated ecommerce video workflows, project ids, uploaded files, or CLI authentication steps.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
