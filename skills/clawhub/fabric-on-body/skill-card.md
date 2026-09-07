## Description:

一键替换服装面料。版式图 + 面料图 -> 换上新面料的样衣图，垂坠与光泽随材质变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, designers, and content-production agents use this skill to preview how a garment style sheet would look in a different fabric before physical sampling. The skill helps produce prompts and commands that preserve the garment silhouette while changing material, texture, sheen, and drape.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, garment images, fabric images, generated outputs, or API credentials may be exposed if the runner is pointed at an untrusted provider endpoint.

Mitigation: Use official provider endpoints, avoid setting ARK_BASE_URL unless the endpoint is fully trusted, and do not run from networks where provider-controlled URL fetches could reach private services.

Risk: Paid image-generation calls may be triggered while testing prompts or provider configuration.

Mitigation: Use dry runs before paid calls and confirm credentials, provider selection, image inputs, and save paths before executing generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated JPEG image files; supports dry-run, batch generation, and provider selection.]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
