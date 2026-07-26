## Description: <br>
A one-stop 1688 sourcing toolkit for product search, bestseller rankings, image-based matching, and authorized procurement workflows from supplier discovery through ordering and logistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, sourcing agents, and e-commerce operators use this skill to search 1688 suppliers, compare wholesale products, run image-based product matching, and complete authorized procurement steps such as order preview, payment link retrieval, order status, logistics, cancellation, and receipt confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys and session metadata may be sent to a configurable gateway. <br>
Mitigation: Use controlled environments, verify the gateway setting before execution, and avoid exposing credentials or generated logs. <br>
Risk: Selected local images may be uploaded to public URLs for image-based search. <br>
Mitigation: Use only intended product images and avoid uploading sensitive, personal, or confidential images. <br>
Risk: Full search or procurement responses may be saved on disk. <br>
Mitigation: Inspect generated linkfox response files before sharing or committing the workspace, and use no-save behavior for procurement responses when appropriate. <br>
Risk: Procurement actions can create orders, request payment links, cancel orders, or confirm receipt. <br>
Mitigation: Require explicit user confirmation for each high-risk action, review the order details before execution, and avoid automatic retries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-sourcing) <br>
- [1688 Product Search Reference](references/linkfox-dld-product-search.md) <br>
- [1688 Product Billboard Reference](references/linkfox-dld-product-billboard.md) <br>
- [1688 Image-Based Product Search Reference](references/linkfox-1688-search-by-image.md) <br>
- [1688 Procurement Workflow Reference](references/linkfox-1688-procurement.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads, shell commands, and optional saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may call LinkFox gateway APIs, upload selected local images to public URLs, and save full or summarized responses under a linkfox output directory depending on script and response size.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
