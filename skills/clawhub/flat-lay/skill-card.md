## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 -> 模特上身商拍图，款式、颜色、织法、版型保持不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and developers use this skill to turn garment flat-lay or existing product photos into on-model catalog images while preserving garment color, texture, fit, and visible details. It guides prompt construction, provider selection, dry-run cost checks, batch generation, and quality review for commercial product imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product or reference images may be sent to an external image-generation provider.

Mitigation: Use --dry-run to inspect the planned request and submit only images and providers approved for the data involved.

Risk: API keys or provider credentials may be exposed if handled carelessly.

Mitigation: Keep keys scoped and revocable, store them through the provider's documented auth flow or environment variables, and rotate them if exposure is suspected.

Risk: Generated model imagery could be misused to imply unauthorized endorsement or commercial likeness rights.

Mitigation: Use owned or licensed reference imagery and avoid creating commercial endorsements with another person's likeness without permission.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline bash and Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated image files locally and can emit JSON status when invoked through the bundled generation script.]

## Skill Version(s):

1.0.12 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
