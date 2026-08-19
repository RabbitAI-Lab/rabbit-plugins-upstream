## Description:

Generates and edits Taobao and Tmall ecommerce product images, including main images, SKU images, detail-page selling-point graphics, ad creatives, background replacement, and product retouching through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent workflows use this skill to plan, generate, edit, and review product image sets for Taobao/Tmall storefronts and advertising. It is intended for product-faithful ecommerce visuals based on user-provided reference images and verified product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product reference images selected by the user are uploaded to AI Hive for generation or editing.

Mitigation: Review each file path before running generate or upload, and avoid sending confidential, unreleased, or unapproved product imagery.

Risk: The skill stores an AI Hive API key locally when initialized.

Mitigation: Use a dedicated API key, keep the local config file restricted, and rotate or revoke the key if the machine or workspace is shared.

Risk: Batch generation and provider routing can incur AI Hive usage charges.

Mitigation: Check batch size, routing mode, and task status before repeating a request; use task lookup for timed-out jobs instead of resubmitting immediately.

Risk: Generated ecommerce images may contain inaccurate text, claims, platform marks, prices, discounts, certifications, or product details.

Mitigation: Verify product structure, packaging, trademarks, text, and compliance against source materials and current marketplace rules before publication.

## Reference(s):

- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples, JSON task responses, and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, accepts local reference image paths, supports batch generation, routing mode, output directory selection, task polling, and optional no-download mode.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
