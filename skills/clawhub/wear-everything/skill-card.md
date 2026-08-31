## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 -> 真人佩戴图，落位、透视与阴影自然。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and creative operators use this skill to turn product and model reference images into on-model accessory product photos for shoes, bags, watches, glasses, hats, scarves, jewelry, and related accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model reference images may be uploaded to dLazy or another configured image provider.

Mitigation: Use only images that are approved for the selected provider, and avoid private or sensitive model photos unless that upload is acceptable.

Risk: Provider API keys or local CLI login may be required to run generation commands.

Mitigation: Store credentials through the documented provider mechanisms, rotate them when needed, and avoid embedding keys in prompts, examples, or saved artifacts.

Risk: The skill is not intended to fabricate another person's endorsement or likeness-based advertising claim.

Mitigation: Use authorized model references and review outputs before publication for consent, placement accuracy, and brand compliance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [gpt-image-2 parameter list](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with CLI commands and image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are saved locally when a save path is provided; cloud providers may also return hosted asset URLs.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
