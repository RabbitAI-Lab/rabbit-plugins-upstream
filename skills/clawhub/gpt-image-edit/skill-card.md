## Description: <br>
Edit images with OpenAI GPT Image 2 on RunComfy by guiding agents to use the RunComfy CLI, model input schema, and prompting patterns for targeted image edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative automation agents use this skill to prepare RunComfy CLI invocations for GPT Image 2 image edits, including preservation edits, multilingual in-image text rewrites, and multi-reference compositions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Edit prompts and publicly fetchable image URLs are sent to RunComfy for processing. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting private images or sensitive embedded text. <br>
Risk: The skill depends on RunComfy CLI authentication through a local login token or RUNCOMFY_TOKEN. <br>
Mitigation: Store tokens only in the expected RunComfy configuration path or environment variable, and avoid exposing them in prompts, logs, or shared shell history. <br>
Risk: Image editing can produce unintended changes to identity, branding, layout, or embedded text. <br>
Mitigation: Review generated outputs before use, and prefer explicit preservation instructions and smaller edit scopes for sensitive assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/gpt-image-edit) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-edit) <br>
- [GPT Image 2 edit endpoint](https://www.runcomfy.com/models/openai/gpt-image-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-edit) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-edit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline JSON and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces RunComfy CLI invocation guidance for the openai/gpt-image-2/edit endpoint; generated image files are produced by the external RunComfy service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
