## Description: <br>
Generate images with Seedream4.5 and videos with Kling via LiblibAI API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benweitu](https://clawhub.ai/user/benweitu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate images, text-to-video clips, image-to-video clips, and task status checks through LiblibAI's Seedream and Kling API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts and image URLs to LiblibAI for remote processing. <br>
Mitigation: Do not include sensitive prompts, private image URLs, regulated data, or internal assets unless they are intended to be processed by LiblibAI. <br>
Risk: The skill requires LiblibAI API credentials. <br>
Mitigation: Install and run it only when LiblibAI use is intended, and provide credentials through environment variables rather than embedding secrets in prompts or files. <br>
Risk: Generated image URLs expire after seven days. <br>
Mitigation: Retrieve and store needed outputs promptly according to the user's retention and compliance requirements. <br>


## Reference(s): <br>
- [LiblibAI API endpoint](https://openapi.liblibai.cloud) <br>
- [ClawHub skill page](https://clawhub.ai/benweitu/skills/liblib-ai-gen) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LiblibAI API credentials; generation jobs are asynchronous and return image or video URLs after polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
