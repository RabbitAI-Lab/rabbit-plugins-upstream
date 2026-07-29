## Description: <br>
Create a self-contained Miao Vision artifact when the user explicitly invokes $miao-vision and supplies an article URL or local Markdown/text for an infographic, or a local CSV, TSV, XLSX, or JSON file for an HTML/PDF report or browser deck. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to turn user-provided article content or local CSV, TSV, XLSX, and JSON files into evidence-grounded infographics, reports, static dashboards, browser decks, PDFs, or validation feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional installer can download and run a local executable, and server security evidence flags the release as suspicious due to a weak trust model around that download. <br>
Mitigation: Review before installing, prefer a trusted preinstalled miao-viz on PATH, avoid overriding MIAO_VISION_RELEASE_REPOSITORY unless the repository is controlled and trusted, and treat first-use installation prompts as high-impact code execution. <br>
Risk: Generated reports, decks, and infographics can include incorrect or misleading analysis if source evidence is weak or untrusted. <br>
Mitigation: Use the skill's strict validation flow, preserve evidence grounding, surface sample warnings, and review generated artifacts before publication or operational use. <br>


## Reference(s): <br>
- [Article Infographic Workflow](references/article.md) <br>
- [Data Report Workflow](references/report.md) <br>
- [Browser Deck Workflow](references/deck.md) <br>
- [Miao Vision Skill Page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured spec guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local HTML, PDF, PNG, YAML, or JSON artifact paths through the Miao Vision CLI when requested.] <br>

## Skill Version(s): <br>
0.1.30 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
