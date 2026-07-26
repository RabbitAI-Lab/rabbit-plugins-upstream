## Description: <br>
Generates AI images through the Infinimo AI Design API with model, aspect ratio, resolution selection, reference uploads, job submission, and result polling for text-to-image, image-to-image, e-commerce creative, and reference-based workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and e-commerce creative teams use this skill to generate or edit product and marketing images through Infinimo AI Design. The skill helps select model settings, upload optional references, submit image jobs, poll for results, and return generated image links with the chosen parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, optional reference images, and the API token are sent to Infinimo/clawec.com for image generation. <br>
Mitigation: Use INFINIMO_TOKEN or INFINIMO_API_KEY from the environment, upload only images intended for the service, and review the service's handling of generated content. <br>
Risk: Generated image records and output URLs may remain visible in the remote service logs. <br>
Mitigation: Review remote logs and deletion controls before use, and delete records through the documented delete endpoint when appropriate. <br>
Risk: Image generation can fail or require credits, returning invalid-token or insufficient-credit responses. <br>
Mitigation: Check API response status and codes, confirm credentials and available credits, and report failures with suggested prompt or account adjustments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/infinimo-ai-design-image-create) <br>
- [Infinimo AI Design](https://design.infinimo.ai/?source=q-i-d-clawhub) <br>
- [Infinimo API key page](https://design.infinimo.ai/api-key?source=q-i-d-clawhub) <br>
- [AI Image Generation Response Schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown summary with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model, aspect ratio, resolution, prompt, reference count, generated image URLs, failure status, and credit usage when returned by the API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
