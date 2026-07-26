## Description: <br>
Generates professional Chinese web-novel cover images by analyzing a title, author name, platform, and genre style, then preparing GPT-Image-2 prompts and image-generation commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create Chinese online-fiction cover art, including genre selection, platform-specific visual style, prompt construction, optional reference-image editing, and local file output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Book titles, author names, generated prompt details, and optional reference images are sent to the configured image API. <br>
Mitigation: Use only an image API endpoint you trust, and avoid confidential manuscripts or private images unless that endpoint is acceptable. <br>
Risk: Generated files are saved under the configured BOOK_DIR path. <br>
Mitigation: Set BOOK_DIR deliberately before execution and review the output path before sharing generated covers or sidecar prompt files. <br>


## Reference(s): <br>
- [Cover Style Reference](references/cover-styles.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/story-cover) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with prompt text and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces prompts, API call commands, PNG cover files, and prompt/reference sidecar text files when executed by an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
