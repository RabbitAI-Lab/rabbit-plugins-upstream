## Description: <br>
Create handheld product short videos via Infinimo AI Design: avatar first-frame compositing, AI script writing, image-to-video submission, and result polling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and e-commerce teams use this skill to generate avatar-led product demo videos and shoppable shorts through the Infinimo AI Design service. The skill helps select an avatar and product image, generate a first frame, optionally create a script, submit image-to-video jobs, and poll for output URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected images, prompts, and generated-video requests to the external Infinimo/clawec service. <br>
Mitigation: Use a scoped API key, review each uploaded file path before running upload_image.sh, and avoid confidential, regulated, customer-sensitive, or unreleased product assets unless external processing is approved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/infinimo-ai-design-product-video-create) <br>
- [Infinimo AI Design](https://design.infinimo.ai/?source=q-i-d-clawhub) <br>
- [Infinimo API Key](https://design.infinimo.ai/api-key?source=q-i-d-clawhub) <br>
- [Handheld Product Video Response Schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON response references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires INFINIMO_TOKEN or INFINIMO_API_KEY and sends selected prompts and images to the Infinimo/clawec API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
