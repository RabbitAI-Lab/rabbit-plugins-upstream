## Description:

多单品融合成一整套 Look。最多 8 张单品图 -> 同一模特身上的完整搭配商拍图，每件单品保真。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and creative operators use this skill to combine up to eight product-item images into a complete modeled outfit image for storefront and campaign use. Agents use it to structure prompts, validate input constraints, and call image-generation tooling for consistent look imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper code can fetch arbitrary user-provided URLs before sending images to external image providers.

Mitigation: Prefer local product image files or trusted image hosts, and avoid internal, private-network, or credential-bearing URLs.

Risk: Generated model appearance defaults may embed unintended ethnicity, gender, age, or appearance choices.

Mitigation: Customize model and brand presets so appearance attributes are intentional for the merchant's use case.

Risk: The skill creates commercial product imagery where product fidelity, missing items, or color mixing can mislead buyers.

Mitigation: Review generated images against every source item before use and rerun with explicit correction prompts when items are omitted or altered.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0 Model Flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy Ecommerce Skills](https://github.com/dlazy-ai/ecommerce-skills)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ordered image inputs, prompt templates, size and resolution flags, optional batching, and optional brand presets.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
