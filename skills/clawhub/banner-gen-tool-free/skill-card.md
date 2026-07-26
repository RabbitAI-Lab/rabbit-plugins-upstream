## Description: <br>
Creates and edits banner illustrations with an image-generation API, supporting 1K, 2K, and 4K outputs and a draft-to-final workflow for personal creators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators use this skill to generate blog and social banners, quick concept images, and style edits from prompts or input images while choosing draft or final resolutions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and input images may be sent to the configured image-generation provider. <br>
Mitigation: Do not use confidential, personal, or proprietary prompts or images unless the provider's data handling terms are acceptable. <br>
Risk: API keys can be exposed if passed directly in commands or shared transcripts. <br>
Mitigation: Set GEMINI_API_KEY through a protected environment variable or secret manager instead of placing keys in prompts or command text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/banner-gen-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell command examples; generated or edited images are saved as PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured image-generation API key, preferably via GEMINI_API_KEY; supports 1K, 2K, and 4K resolution choices.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
