## Description: <br>
Story Cover helps agents create Chinese web-novel covers by selecting genre and platform styling, building GPT-Image prompts, calling an image API, and saving the generated cover assets locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authors, editors, and publishing teams use this skill to generate professional-looking Chinese web-novel cover concepts from a title, author name, target platform, and optional reference image. It guides the agent through prompt construction, image generation, local file output, platform-specific resizing, and quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Book titles, author names, prompts, and optional reference images may be sent to the configured image API. <br>
Mitigation: Use only a trusted GPT_IMAGE_BASE_URL endpoint and avoid submitting sensitive or unlicensed reference material. <br>
Risk: Generated cover images and prompt text are saved locally in the configured book directory. <br>
Mitigation: Choose a BOOK_DIR appropriate for storing generated cover assets and review outputs before publication or upload. <br>


## Reference(s): <br>
- [Story Cover on ClawHub](https://clawhub.ai/worldwonderer/skills/story-cover) <br>
- [Publisher profile](https://clawhub.ai/user/worldwonderer) <br>
- [Source link from metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Cover style reference](references/cover-styles.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with bash command blocks plus locally saved PNG cover files and prompt text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GPT_IMAGE_API_KEY and the curl, jq, and base64 command-line tools; BOOK_DIR controls where generated cover files are saved, with optional GPT_IMAGE_BASE_URL, GPT_IMAGE_MODEL, GPT_IMAGE_SIZE, UPLOAD_SIZE, and REF_IMAGE settings.] <br>

## Skill Version(s): <br>
1.1.5 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
