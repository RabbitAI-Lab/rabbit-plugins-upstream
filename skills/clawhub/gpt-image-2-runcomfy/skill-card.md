## Description: <br>
Generates and edits images with OpenAI's GPT Image 2 through the RunComfy CLI, including text-to-image and image-edit workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and creative teams use this skill to prepare RunComfy CLI requests for GPT Image 2 image generation, image editing, brand mockups, localized graphics, and prompt iteration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference image URLs are sent to RunComfy for processing. <br>
Mitigation: Use the skill only for content approved for RunComfy processing and avoid sensitive prompts or private image URLs. <br>
Risk: A broad trigger phrase such as "GPT Image" can route an ambiguous request to GPT Image 2. <br>
Mitigation: Confirm the intended model when the user does not explicitly request GPT Image 2. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/gpt-image-2-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy GPT Image 2 text-to-image](https://www.runcomfy.com/models/openai/gpt-image-2/text-to-image?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-2-runcomfy) <br>
- [RunComfy GPT Image 2 edit](https://www.runcomfy.com/models/openai/gpt-image-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-2-runcomfy) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-2-runcomfy) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=gpt-image-2-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with bash commands and JSON RunComfy inputs; RunComfy writes generated image files to the requested output directory.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runcomfy CLI, a RunComfy login or RUNCOMFY_TOKEN, and publicly fetchable HTTPS image URLs for edit references.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
