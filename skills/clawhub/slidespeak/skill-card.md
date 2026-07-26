## Description: <br>
Generate, edit, and manage PowerPoint presentations via the SlideSpeak API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mve](https://clawhub.ai/user/mve) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other agent users use this skill to create presentations from text or uploaded documents, edit existing presentations, list templates, and retrieve generated PowerPoint download links through SlideSpeak. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Presentation prompts, selected local documents, and slide configuration data are sent to the external SlideSpeak service. <br>
Mitigation: Use the skill only with documents and prompts approved for SlideSpeak processing, and avoid confidential or regulated content unless that use is authorized. <br>
Risk: The skill requires a SlideSpeak API key for all API calls. <br>
Mitigation: Store SLIDESPEAK_API_KEY as a secret, do not paste it into prompts or generated files, and rotate it if exposure is suspected. <br>
Risk: Slide removal and webhook subscription commands can change presentation state or send task notifications to a user-provided endpoint. <br>
Mitigation: Review presentation IDs, slide positions, edit types, and webhook URLs before running REMOVE or webhook commands. <br>


## Reference(s): <br>
- [SlideSpeak API Reference](references/API.md) <br>
- [SlideSpeak homepage](https://slidespeak.co) <br>
- [SlideSpeak on ClawHub](https://clawhub.ai/mve/skills/slidespeak) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SLIDESPEAK_API_KEY and returns task IDs, task status, generated presentation metadata, and short-lived download URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
