## Description: <br>
Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ningzimu](https://clawhub.ai/user/ningzimu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and presentation authors use this skill to turn source material into unified, image-based PowerPoint decks with slide prompts, generated slide images, speaker notes, and final PPTX assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Slide prompts or selected source images may be sent to a configured remote image API. <br>
Mitigation: Use the built-in image tool when possible, avoid untrusted third-party API base URLs, and review sensitive content before generation. <br>
Risk: The skill creates persistent project files, prompts, intermediate images, and PPTX outputs on the local filesystem. <br>
Mitigation: Set an explicit output folder for sensitive work and clean generated prompts and intermediate files after use. <br>
Risk: CLI fallback can store API settings in ~/.codex-ppt-skill/.env and install Python dependencies into a shared local virtual environment. <br>
Mitigation: Review local configuration before use and install only when the shared runtime and persisted settings are acceptable. <br>


## Reference(s): <br>
- [Codex PPT ClawHub page](https://clawhub.ai/ningzimu/skills/codex-ppt) <br>
- [Codex PPT homepage](https://github.com/ningzimu/codex-ppt-skill) <br>
- [Backend selection](docs/backend-selection.md) <br>
- [Image model configuration](docs/image-model-configuration.md) <br>
- [Project assembly and reporting](docs/project-assembly-and-reporting.md) <br>
- [Slide generation and subagents](docs/slide-generation-and-subagents.md) <br>
- [Style library](docs/style-library.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON prompt/state files, generated slide images, speaker notes, and PPTX deck files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create persistent project files and use a configured image backend for slide image generation.] <br>

## Skill Version(s): <br>
0.5.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
