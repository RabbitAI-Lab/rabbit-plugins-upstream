## Description:

Product Video turns product photos, product links, specifications, manuals, or catalogs into product demo, showcase, or advertising videos through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy product-video projects for e-commerce ads, shopping videos, product demonstrations, and cross-border selling content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and attached files are sent to dLazy service endpoints.

Mitigation: Upload only product assets that are appropriate to share with the dLazy hosted service.

Risk: Authentication stores a dLazy API key in local CLI configuration unless the environment variable path is used.

Mitigation: Use per-invocation credentials where appropriate, protect the local config file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm install leaves the dLazy CLI installed on the system.

Mitigation: Use the pinned npx invocation instead of a global install when lower local persistence is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and dLazy CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the product-to-ecommerce-video dLazy template and may upload attached local files through the dLazy CLI.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
