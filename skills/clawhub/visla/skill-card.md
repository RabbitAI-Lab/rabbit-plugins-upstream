## Description: <br>
Creates AI-generated videos from text scripts, URLs, PPT/PDF documents, ideas, visual resources, or speech using Visla, and supports account credit, avatar, and voice checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visla-admin](https://clawhub.ai/user/visla-admin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate Visla videos from scripts, URLs, documents, ideas, images, video, or speech, and to check Visla account credits, avatars, and voices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected scripts, URLs, documents, images, videos, or audio to Visla for processing. <br>
Mitigation: Use it only with content approved for Visla processing and avoid confidential or regulated files unless policy allows it. <br>
Risk: The skill requires Visla API credentials and can read saved credentials after user approval. <br>
Mitigation: Use a dedicated Visla API key when possible, never echo secrets in normal chat output, and approve saved-credential access only when expected. <br>
Risk: Video generation can take several minutes and may time out before completion. <br>
Mitigation: Run with a timeout of at least 30 minutes when possible and use the returned project UUID to continue checking status if a timeout occurs. <br>


## Reference(s): <br>
- [Visla API Key and Secret](https://www.visla.us/visla-api) <br>
- [ClawHub skill page](https://clawhub.ai/visla-admin/skills/visla) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown status updates, command invocations, JSON configuration examples, and video download links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Visla API credentials and may upload user-selected scripts, URLs, documents, images, videos, or audio to Visla for processing.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
