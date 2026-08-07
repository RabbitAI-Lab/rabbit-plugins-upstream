## Description: <br>
Helps agents create ecommerce product images by tailoring prompts for hero, scene, model, and white-background images, then using Lingxiao's paid MCP image generation service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mikeli20221102-ux](https://clawhub.ai/user/mikeli20221102-ux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce sellers and operators use this skill to prepare product-image prompts, select image models, check pricing and balance, and generate single paid product images for listing or advertising workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and account-authenticated image generation requests are sent to Lingxiao's MCP service. <br>
Mitigation: Install only when this third-party service use is acceptable, and keep the Lingxiao API key private. <br>
Risk: Image generation can spend the user's paid Lingxiao image-generation balance. <br>
Mitigation: Check available models, per-image pricing, and account balance before generation, and use confirm: true only when the spend is intended. <br>
Risk: AI-generated ecommerce images may misrepresent product details or create copyright, likeness, brand, or marketplace compliance issues. <br>
Mitigation: Review generated images before publication, use real photography for material-critical listing images, and verify applicable rights and platform rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mikeli20221102-ux/skills/lingxiao-image-generate) <br>
- [Lingxiao MCP endpoint](https://www.lingxiaochuhai.com/mcp) <br>
- [Lingxiao membership and API key page](https://www.lingxiaochuhai.com/app/membership?from=mcp-trial) <br>
- [Lingxiao visual factory](https://www.lingxiaochuhai.com/tools/visual-factory) <br>
- [Lingxiao one-click outfit](https://www.lingxiaochuhai.com/tools/one-click-outfit) <br>
- [Lingxiao link builder](https://www.lingxiaochuhai.com/tools/link-builder) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API Calls, Markdown, Text] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include billing, model, balance, downgrade, and reference-image status returned by the Lingxiao service.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
