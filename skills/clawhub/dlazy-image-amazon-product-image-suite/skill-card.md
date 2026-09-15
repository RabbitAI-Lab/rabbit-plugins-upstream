## Description:

A professional product image generation skill for Amazon product detail pages, covering main images, secondary images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace teams, and ecommerce creative operators use this skill to plan and generate Amazon-compliant product image sets, including main images, secondary infographics, lifestyle/detail shots, and A+ content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run a third-party npm CLI with user-account permissions.

Mitigation: Prefer npx or a local install, review @dlazy/cli@1.2.3 and its source before use, and avoid global installation unless operationally required.

Risk: The CLI stores persistent dLazy credentials in a local configuration file or reads them from DLAZY_API_KEY.

Mitigation: Use least-privilege API keys where possible, protect the local config file, and rotate or revoke keys if the CLI or environment is no longer trusted.

Risk: Prompts and user-provided media paths may be sent to dLazy API and uploaded to files.dlazy.com for generation.

Mitigation: Provide only product media and prompts intended for upload to the dLazy service, and avoid confidential or regulated content unless approved for that service.

Risk: Server evidence reports unavailable provenance and disclosure inconsistencies.

Mitigation: Treat repository and package links as metadata references, verify the publisher and package independently before deployment, and do not infer GitHub import provenance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, checklists, prompt drafts, and generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the dLazy CLI, upload user-provided media paths, and return generated result URLs hosted by files.dlazy.com.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
