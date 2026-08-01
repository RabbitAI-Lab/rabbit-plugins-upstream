## Description: <br>
Guides an agent through precise single-image local edits with Flux 1 Kontext Pro on RunComfy, including model routing, prompt patterns, input schema, prerequisites, and CLI invocation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to prepare and execute single-source-image edits with Flux 1 Kontext Pro through RunComfy. It is most useful for targeted local edits, source identity preservation, prompt shaping, and choosing when to route to adjacent image-editing models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and source image URLs are sent to RunComfy for image editing. <br>
Mitigation: Use content that is appropriate for RunComfy processing and avoid sensitive prompts or images unless the deployment policy permits that data flow. <br>
Risk: The short trigger term "kontext" can be ambiguous. <br>
Mitigation: For ambiguous requests, confirm that the user intends the RunComfy Flux Kontext image-editing model before invoking it. <br>
Risk: External image URLs and generated media can carry untrusted content risks. <br>
Mitigation: Treat source URLs and generated outputs as untrusted, review outputs before use, and follow the skill's documented download and endpoint boundaries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/permew/skills/flux-kontext) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI Introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-kontext) <br>
- [Flux 1 Kontext Pro Model Page](https://www.runcomfy.com/models/blackforestlabs/flux-1-kontext-pro/image-to-image?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-kontext) <br>
- [RunComfy CLI Troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=flux-kontext) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When the generated commands are executed, the RunComfy CLI can download generated image files into the requested output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
