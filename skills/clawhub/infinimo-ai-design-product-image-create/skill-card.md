## Description: <br>
Generate e-commerce product images (hero, secondary, A+ detail) via Infinimo AI Design with marketplace selection, model/aspect/resolution options, reference uploads, job submission, and result polling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce operators, designers, and developers use this skill to create marketplace-ready product imagery for Amazon, Shopify, and similar listings by selecting platform and market settings, uploading optional references, submitting generation jobs, and polling returned image URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, product images, reference URLs, and the Infinimo API token are sent to the clawec.com/Infinimo service. <br>
Mitigation: Use this skill only when that data sharing is acceptable, keep tokens in environment variables, and avoid confidential, regulated, or customer-identifying assets unless approved. <br>
Risk: The documented delete endpoint can remove generated image log entries. <br>
Mitigation: Treat deletion as a manual destructive action and confirm the target ID before using it. <br>


## Reference(s): <br>
- [Product Image Design Response Schema](references/response-schema.md) <br>
- [Infinimo AI Design](https://design.infinimo.ai/?source=q-i-d-clawhub) <br>
- [Infinimo API Key](https://design.infinimo.ai/api-key?source=q-i-d-clawhub) <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/infinimo-ai-design-product-image-create) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash commands and JSON response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses INFINIMO_TOKEN or INFINIMO_API_KEY for API access; generated image results are returned as URLs after polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
