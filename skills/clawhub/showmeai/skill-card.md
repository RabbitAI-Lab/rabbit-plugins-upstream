## Description: <br>
Generate and edit images, create videos, convert images to 3D, synthesize speech or music, and process images through ShowMeAI for agents that create media, configure models, inspect token-group availability, or resume generation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hulebaji](https://clawhub.ai/user/hulebaji) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and teams use this skill to route creative-media requests through ShowMeAI while keeping API-key setup, model defaults, polling, recovery, and local downloads consistent across Python-capable agent hosts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that result downloads can send the user's ShowMeAI API key to result URLs outside the ShowMeAI API. <br>
Mitigation: Before installing, confirm the configured base URL is trusted and ask the publisher to restrict Authorization headers to trusted ShowMeAI API endpoints. <br>
Risk: The skill stores a ShowMeAI API key locally and sends selected prompts or files to ShowMeAI. <br>
Mitigation: Use the skill only in a trusted local environment, pass the key through hidden input or standard input, and avoid sending files or prompts that should not be processed by ShowMeAI. <br>


## Reference(s): <br>
- [ShowMeAI API homepage](https://api.showmeai.art) <br>
- [ShowMeAI API documentation](https://showmeai.apifox.cn) <br>
- [Configuration and credentials](references/configuration.md) <br>
- [Image generation and editing](references/image.md) <br>
- [Video generation](references/video.md) <br>
- [Image to 3D](references/three-d.md) <br>
- [Speech and music](references/audio.md) <br>
- [Image tools](references/image-tools.md) <br>
- [Durable polling and recovery](references/polling.md) <br>
- [Architecture and design](DESIGN.md) <br>
- [Release history](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown or plain text guidance with shell commands, JSON command results, and local media file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful media workflows return downloaded local files and MEDIA path lines; long-running jobs may require polling or task resume.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
