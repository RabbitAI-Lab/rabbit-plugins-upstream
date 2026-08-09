## Description: <br>
Image helps agents create, edit, and optimize marketing images such as blog heroes, social graphics, product mockups, banners, brand assets, and OG images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketing teams, founders, and developers use this skill to select image-production workflows, draft AI image prompts, create screenshot-based mockups, generate social and OG image guidance, and optimize web image formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to upload product screenshots, brand assets, or private product context to third-party image or design services. <br>
Mitigation: Review assets before upload, remove sensitive data from screenshots, and share only the minimum private context needed for the task. <br>
Risk: Some recommended image-generation providers require API keys or paid usage. <br>
Mitigation: Use project-scoped credentials, avoid pasting secrets into prompts, and confirm provider pricing before generating images at scale. <br>
Risk: AI image models can hallucinate product interfaces or render text inaccurately. <br>
Mitigation: Use real screenshots for product UI, add text and logos during post-processing when exact branding matters, and review final assets before publication. <br>


## Reference(s): <br>
- [AI Image Prompting Guide](references/ai-image-prompting.md) <br>
- [ClawHub image skill page](https://clawhub.ai/coreyhaines31/skills/image) <br>
- [Gemini API image generation documentation](https://ai.google.dev/gemini-api/docs/image-generation) <br>
- [Black Forest Labs API documentation](https://docs.bfl.ai/) <br>
- [Ideogram API documentation](https://developer.ideogram.ai/) <br>
- [OpenAI image generation documentation](https://platform.openai.com/docs/guides/image-generation) <br>
- [Recraft API documentation](https://www.recraft.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with prompts, workflow steps, code snippets, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend third-party image-generation, design, screenshot, CDN, and optimization tools depending on user context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
