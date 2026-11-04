## Description:

Generates vector graphics from text prompts through the dLazy-hosted Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the skill to generate scalable vector artwork such as logos and icons from text prompts, then receive or save the generated asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media supplied to the service are processed by dLazy, and generation may incur usage charges.

Mitigation: Submit only content you intend to share with dLazy and review expected charges before generating.

Risk: The external CLI package and its credential-protection claims have not been verified in the security review.

Mitigation: Keep the CLI pinned to the documented version, protect the saved API key, and rotate or revoke it if exposed.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits settings](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Files, Images]

**Output Format:** [Generated vector artwork returned through a JSON response with hosted asset URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A generated image asset can be saved to a local path; asynchronous requests can return a task identifier before the asset is ready.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
