## Description: <br>
Creates self-contained local-first Miao Vision artifacts from article URLs or local Markdown/text as infographics, and from local CSV, TSV, XLSX, or JSON files as HTML/PDF reports or browser decks, and can validate report or deck specs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to turn local articles or data files into evidence-grounded visual artifacts such as infographics, reports, browser decks, and validated report or deck specs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can be redirected to download a CLI binary from a repository selected through MIAO_VISION_RELEASE_REPOSITORY. <br>
Mitigation: Use a preinstalled trusted miao-viz CLI when possible, and run the installer only when MIAO_VISION_RELEASE_REPOSITORY is unset or intentionally points to a trusted repository. <br>
Risk: The shared Miao Vision CLI remains installed after plugin upgrades or uninstalls. <br>
Mitigation: Delete the shared Miao Vision home directory when full removal of the installed CLI is required. <br>


## Reference(s): <br>
- [Miao Vision Skill Definition](SKILL.md) <br>
- [Article Infographic Workflow](references/article.md) <br>
- [Data Report Workflow](references/report.md) <br>
- [Browser Deck Workflow](references/deck.md) <br>
- [Miao Vision Plugin Installation](install/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or YAML specs; rendered artifacts may be HTML, PDF, PNG, or browser deck files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-first workflows; PDF and PNG export may require Playwright, and installation or network fetches require explicit approval.] <br>

## Skill Version(s): <br>
0.2.1 (source: release evidence and install/README.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
