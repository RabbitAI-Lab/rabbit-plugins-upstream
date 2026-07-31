## Description: <br>
AI image generation on RunComfy that routes text-to-image and image-to-image requests across supported RunComfy model endpoints and provides prompting guidance plus `runcomfy run` commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to choose RunComfy image-generation or image-editing models, shape prompts, and produce RunComfy CLI commands for generating or restyling images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunComfy CLI requests may consume the user's RunComfy account credits or use stored RunComfy authentication. <br>
Mitigation: Confirm the selected model, inputs, output directory, and account context before running expensive or ambiguous generation requests. <br>
Risk: Reference URLs or web grounding can influence generation results in ways the user did not intend. <br>
Mitigation: Use only user-provided reference URLs and enable web grounding only when the user explicitly asks for real-world grounding. <br>
Risk: Ambiguous image prompts can route to an unsuitable model or endpoint. <br>
Mitigation: Ask a clarifying question when the desired workflow, reference images, edit scope, or model choice is unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/ai-image-generation-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy model catalog](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>
- [RunComfy CLI introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>
- [RunComfy CLI install](https://docs.runcomfy.com/cli/install?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>
- [RunComfy CLI quickstart](https://docs.runcomfy.com/cli/quickstart?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>
- [RunComfy CLI commands](https://docs.runcomfy.com/cli/commands?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>
- [RunComfy CLI auth](https://docs.runcomfy.com/cli/auth?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=ai-image-generation-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash commands and model-specific parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for RunComfy CLI invocations and output directory selection; generated image files are produced by the RunComfy CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
