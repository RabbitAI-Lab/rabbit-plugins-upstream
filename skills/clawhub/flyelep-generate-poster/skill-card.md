## Description:

Generates e-commerce product hero images, detail-page posters, and white-background product images through the Flyelep API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect product-generation parameters, call Flyelep's asynchronous poster-generation API, poll for task completion, and return generated image URLs for e-commerce product imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flyelep API keys may be exposed through local temp files, inline shell commands, logs, or command history.

Mitigation: Use a secret-handling method that avoids writing keys to payload_temp.json or embedding them directly in shell commands, delete any temporary payload files, and rotate the key if exposure is possible.

Risk: Product descriptions and reference image URLs are sent to Flyelep for image generation.

Mitigation: Install and use the skill only when users are comfortable sending that content to Flyelep.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-generate-poster)
- [Flyelep publisher profile](https://clawhub.ai/user/flyelepai)
- [Flyelep platform](https://www.flyelep.cn)
- [Flyelep generateAsync API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/generateAsync)
- [Flyelep queryTaskResult API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with JSON request bodies, shell commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses asynchronous task submission and polling; generated images are returned as URLs rather than embedded image content.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
