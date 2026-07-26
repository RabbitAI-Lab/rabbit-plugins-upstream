## Description: <br>
Analyzes a provided product list with multimodal AI to group products by main-image similarity for visual clustering, deduplication, and competitor lookalike detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers and ecommerce analysts use this skill to post-process product search or recommendation results, grouping items by visual similarity and highlighting same-style, duplicate, or cross-brand lookalike products. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product metadata, image URLs, prior tool output, and user prompts are sent to LinkFox services. <br>
Mitigation: Use only with data approved for LinkFox processing, and avoid confidential catalog or customer data unless the gateway environment and data handling are understood. <br>
Risk: Full API responses can be persisted in local LinkFox session and cache directories. <br>
Mitigation: Review where response files are stored, limit access to the workspace, and delete cached or saved responses that contain sensitive product data. <br>
Risk: The skill can automatically report feedback and may send context about behavior or user satisfaction to a separate LinkFox feedback endpoint. <br>
Mitigation: Disable or avoid feedback reporting where user prompts, business context, or result details should not leave the environment. <br>
Risk: Calls consume LinkFox credits and repeated analysis can create unexpected cost. <br>
Mitigation: Confirm cost-sensitive runs with the user, reuse cached results when appropriate, and avoid repeated retries with changed parameters unless the user approves. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-product-similarity) <br>
- [API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and tables with saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a prior products array; large responses are summarized on stdout unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
