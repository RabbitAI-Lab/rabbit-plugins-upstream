## Description:

Generate Poster helps agents call the Flyelep API to create e-commerce product main images, detail-page posters, and white-background product images using asynchronous polling or synchronous image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect e-commerce image-generation requirements, prepare optional reference images, call Flyelep poster-generation endpoints, and return generated image URLs for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Flyelep API key to call the service.

Mitigation: Provide the API key only at runtime and do not place real secrets in saved examples or shared files.

Risk: Product images supplied by the user may be uploaded to Flyelep and made available through a permanent public URL.

Mitigation: Upload only product images the user is comfortable sending to Flyelep and exposing through a public image link.

Risk: Synchronous generation can time out or disconnect before a result is returned, and that mode does not provide a task ID for later lookup.

Mitigation: Prefer asynchronous generation with polling unless the user explicitly needs a single blocking request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/flyelepai/skills/flyelep-generate-poster)
- [Flyelep asynchronous poster generation endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/generateAsync)
- [Flyelep task result query endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)
- [Flyelep synchronous poster generation endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/generate)
- [Flyelep file upload endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with JSON payload examples and curl commands; Flyelep returns generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Flyelep secretKey at runtime; synchronous generation can hold a request open for up to 15 minutes.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
