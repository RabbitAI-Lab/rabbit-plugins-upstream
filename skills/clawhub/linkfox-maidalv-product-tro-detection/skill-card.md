## Description: <br>
Checks product images, descriptions, reference images, and IP keywords with LinkFox's 卖大律 service to assess TRO and trademark, patent, or copyright infringement risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cross-border e-commerce sellers, marketplace operators, and compliance reviewers use this skill before listing a product to identify possible TRO, trademark, patent, or copyright risk from a product image and supporting text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product images, descriptions, IP keywords, and local image uploads are sent to LinkFox services. <br>
Mitigation: Use only inputs approved for third-party processing, and avoid sensitive or confidential product data unless the LinkFox service terms are acceptable. <br>
Risk: Full API responses and cache files may be saved locally under linkfox directories. <br>
Mitigation: Review saved outputs for sensitive data and delete response or cache files when they are no longer needed. <br>
Risk: The LINKFOX_TOOL_GATEWAY environment variable can redirect requests to a custom endpoint. <br>
Mitigation: Leave LINKFOX_TOOL_GATEWAY unset unless the destination is trusted and expected. <br>
Risk: The skill includes automatic feedback reporting and an external onboarding-skill installation path. <br>
Mitigation: Review or disable those workflows before using the skill in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-maidalv-product-tro-detection) <br>
- [卖大律 API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON risk assessment saved locally, with inline JSON or a concise Markdown-readable summary depending on response size.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes overall risk level, high-risk items, lower-risk IP matches, TRO plaintiff details when available, numeric risk scores, and an AI-generated legal assessment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
