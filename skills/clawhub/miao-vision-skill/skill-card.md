## Description: <br>
Creates local-first Miao Vision artifacts from explicitly supplied article, text, or structured-data inputs, including infographics, HTML/PDF reports, browser decks, recurring reports, and report or deck spec validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill in local agent environments to turn provided article content or local structured datasets into grounded visualization artifacts and to validate Miao Vision specs before rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may download and keep a local Miao Vision executable under ~/.miao-vision/bin. <br>
Mitigation: Approve installation only after confirming the download is expected, and remove ~/.miao-vision manually when the shared CLI is no longer wanted. <br>
Risk: The skill can process local files and user-provided article URLs. <br>
Mitigation: Use it only with files or URLs you intentionally provide, and review approval prompts before any installation or optional PDF dependency step. <br>
Risk: Generated reports, decks, and infographics can be misleading if source evidence is incomplete or interpreted too broadly. <br>
Mitigation: Keep claims grounded in the provided data or article content, run strict validation before rendering, and surface blocking validation or PDF export errors instead of bypassing them. <br>


## Reference(s): <br>
- [Article Infographic Workflow](references/article.md) <br>
- [Data Report Workflow](references/report.md) <br>
- [Browser Deck Workflow](references/deck.md) <br>
- [Miao Vision Plugin Installation](install/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON/YAML specs, and generated HTML, PDF, PNG, or browser-deck files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are grounded in user-provided source evidence and validated with the resolved local Miao Vision CLI when rendering artifacts.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
