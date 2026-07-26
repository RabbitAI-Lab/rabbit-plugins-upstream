## Description: <br>
Create complete AI music videos from local audio or public audio URLs with 1-7 reference images for single-track or batch production through the official BizMuse CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bizmuse-ai](https://clawhub.ai/user/bizmuse-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn finished songs plus visual references into AI-generated music videos, monitor BizMuse generation tasks, and download completed video or cover assets. It supports single-track production and bounded batch runs for directories of audio files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uploads selected audio, reference images, prompts, and generated media to the external BizMuse service. <br>
Mitigation: Confirm the user has the right to upload and process the supplied media, and upload only the files required for the requested video. <br>
Risk: Generation requires a BizMuse account, API key, and paid generation credits. <br>
Mitigation: Have users configure API keys locally with the BizMuse CLI, never paste credentials into chat, and direct billing or credit issues to BizMuse account controls. <br>
Risk: Model output may not preserve exact subject identity, wardrobe, or scene consistency. <br>
Mitigation: Set expectations before submission and use clear, well-lit reference images when consistency matters. <br>


## Reference(s): <br>
- [BizMuse Skill Documentation](https://bizmuse.ai/skill) <br>
- [BizMuse Product](https://bizmuse.ai) <br>
- [BizMuse Pricing](https://bizmuse.ai/pricing) <br>
- [Setup and Input Requirements](references/setup.md) <br>
- [Supported Model and Controls](references/models.md) <br>
- [Music Video Prompt Guide](references/prompts.md) <br>
- [Error Handling](references/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash commands and concise task status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, status, video and cover URLs, download paths, batch manifest paths, and provider or account errors without exposing credentials.] <br>

## Skill Version(s): <br>
1.1.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
