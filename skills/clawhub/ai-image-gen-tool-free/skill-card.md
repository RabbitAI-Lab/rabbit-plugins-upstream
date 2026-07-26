## Description: <br>
Generates images from text prompts with multiple aspect ratios and standard resolution options for personal creators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and agent users use this skill to generate basic images from text prompts for avatars, social media artwork, video covers, and creative ideation. It requires a configured external image API key and command-line execution capability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and generated-image requests are sent to a user-configured third-party image API. <br>
Mitigation: Avoid including secrets, personal data, confidential business details, or regulated information in prompts. <br>
Risk: The artifact references a Python generator script that is not included in the release evidence. <br>
Mitigation: Supply or verify the script separately before executing any generated command. <br>
Risk: Generated image output can be incorrect, misleading, or unsuitable for high-stakes use. <br>
Mitigation: Review generated images manually and do not use the skill for medical, legal, or deterministic decision-making workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-image-gen-tool-free) <br>
- [Configured image API endpoint](https://code.newcli.com/gemini) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to produce or save image files through a user-configured external image API; the referenced generator script is not included in the artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
