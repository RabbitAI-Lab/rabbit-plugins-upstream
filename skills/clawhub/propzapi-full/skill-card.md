## Description: <br>
Generate images from HTML/CSS templates and capture webpage screenshots via propzapi.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paperandbeyond23-gif](https://clawhub.ai/user/paperandbeyond23-gif) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to render deterministic HTML/CSS assets such as Open Graph images, social cards, certificates, invoices, charts, and screenshots. It is suited for workflows that need template-based rendering or webpage capture rather than prompt-based image generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Template contents, render variables, created templates, and screenshot target URLs are sent to PropzAPI. <br>
Mitigation: Avoid sending secrets, personal data, private dashboard URLs, or tokenized links unless that data sharing is approved for the use case. <br>
Risk: Screenshot capture can involve third-party or access-controlled pages. <br>
Mitigation: Confirm rights, site terms, and authorization before capturing pages, especially pages that are private or user-specific. <br>
Risk: Rendered image and screenshot calls consume PropzAPI credits. <br>
Mitigation: Confirm render intent before paid operations and use free operations such as listing templates, creating templates, or signing embed URLs when those meet the task. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/paperandbeyond23-gif/skills/propzapi-full) <br>
- [PropzAPI homepage](https://propzapi.com) <br>
- [PropzAPI documentation](https://propzapi.com/docs) <br>
- [PropzAPI OpenAPI specification](https://api.propzapi.com/openapi.json) <br>
- [PropzAPI MCP server](https://api.propzapi.com/mcp) <br>
- [PropzAPI pricing](https://propzapi.com/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, image URLs, configuration, guidance] <br>
**Output Format:** [JSON responses with rendered asset URLs and metadata, plus Markdown or plain-text guidance for setup and errors] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Rendered outputs may be PNG, JPEG, WEBP, or PDF; image generation and screenshot calls consume PropzAPI credits.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
