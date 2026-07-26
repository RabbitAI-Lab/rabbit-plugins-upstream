## Description: <br>
Bria.ai image API skill for generating images from prompts, editing images with natural language, removing backgrounds, and creating product lifestyle shots through authenticated Bria API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galbria](https://clawhub.ai/user/galbria) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, designers, and content teams use this skill to call Bria image APIs for commercial image generation, background removal, product photography, image editing, restoration, and upscaling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected images, image URLs, and prompts to Bria's external service for processing. <br>
Mitigation: Use it only with data approved for Bria processing; avoid confidential or regulated images unless Bria is approved for that data. <br>
Risk: The authentication flow caches Bria access and API tokens under ~/.bria/credentials. <br>
Mitigation: Restrict credential-file permissions, remove cached credentials when no longer needed, and revoke tokens from the Bria account if exposure is suspected. <br>
Risk: API calls require an active Bria account and may fail on billing, quota, token, moderation, timeout, or server errors. <br>
Mitigation: Verify billing status before calls, stop on billing errors, re-authenticate expired tokens, and review failed or timed-out requests before retrying. <br>


## Reference(s): <br>
- [Bria Homepage](https://bria.ai) <br>
- [Full API docs for agents](https://docs.bria.ai/llms.txt) <br>
- [Capabilities & Prompt Recipes](references/capabilities.md) <br>
- [API Endpoints Reference](references/api-endpoints.md) <br>
- [Shell Client](references/code-examples/bria_client.sh) <br>
- [Auth Helper](references/code-examples/bria_auth.sh) <br>
- [ClawHub skill page](https://clawhub.ai/galbria/skills/bria-ai) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/galbria) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with bash snippets, configuration steps, and Bria image result URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and Bria credentials; some image operations return asynchronous status URLs that are polled until an image URL is available.] <br>

## Skill Version(s): <br>
1.3.1 (source: ClawHub release evidence; artifact metadata reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
