## Description:

Refines existing product photos with GPT Image 2 through AI Hive, using a defect list and locked product attributes to control dust removal, scratch reduction, reflection cleanup, color correction, label protection, and background cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants, e-commerce operators, and creative teams use this skill to retouch product images while preserving commercially important details such as shape, labels, logos, package quantities, approved colors, and real wear. It is suited for product-photo post-production workflows that require before-and-after review and prompt records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are uploaded to AI Hive for generation.

Mitigation: Use only images and prompt content that the user is permitted to send to AI Hive, and avoid sensitive or unreleased product information unless that transfer is approved.

Risk: The helper can store an AI Hive API key in a local configuration file.

Mitigation: Prefer short-lived or scoped keys where available, keep the config file private, and rotate the key if the local environment is shared or compromised.

Risk: Image editing could unintentionally alter labels, logos, colors, real damage, or other product details that affect buyer expectations.

Mitigation: Review the defect list, immutable details, prompt, original image, and generated result before publication or commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-retouch)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Images, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task responses from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one reference image and an AI Hive API key; generated images are downloaded to a local output directory unless disabled.]

## Skill Version(s):

1.0.0 (source: server release evidence, created 2026-08-17T14:34:53.678Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
