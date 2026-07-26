## Description: <br>
Call fal.ai model APIs for image generation (text-to-image and image-to-image). Use when a user asks to integrate fal, construct requests, run jobs, handle auth, or return image URLs from fal model APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xxmzdxxxm](https://clawhub.ai/user/xxmzdxxxm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to integrate fal.ai text-to-image and image-to-image model APIs, construct SDK or REST requests, handle authentication, and return generated image URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: fal.ai API keys may be exposed if copied into code, chat transcripts, or request examples. <br>
Mitigation: Keep the fal API key in environment variables and avoid hardcoding credentials in generated snippets. <br>
Risk: Prompts or source images submitted to fal.ai may contain sensitive content. <br>
Mitigation: Review prompts and images before submitting jobs, and avoid sending content that should not be processed by fal.ai. <br>
Risk: Model-specific request schemas and output fields may differ from the included templates. <br>
Mitigation: Verify the selected model's current documentation before constructing requests or parsing image URLs. <br>


## Reference(s): <br>
- [Fal Model API Checklist](artifact/references/fal-model-api-checklist.md) <br>
- [fal Model API Examples](artifact/references/fal-model-examples.md) <br>
- [fal Model APIs Quickstart](https://docs.fal.ai/model-apis/quickstart) <br>
- [Generate Images from Text](https://docs.fal.ai/model-apis/guides/generate-images-from-text) <br>
- [fal Client Libraries](https://docs.fal.ai/model-apis/client) <br>
- [fal Model Endpoints](https://docs.fal.ai/model-apis/model-endpoints) <br>
- [fal Queue Endpoints](https://docs.fal.ai/model-apis/model-endpoints/queue) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API calls] <br>
**Output Format:** [Markdown with Python, JavaScript, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include generated image URL lists and requested metadata such as seed or image size when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
