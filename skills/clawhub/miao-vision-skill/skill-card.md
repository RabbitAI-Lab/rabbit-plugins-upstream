## Description: <br>
Miao Vision helps agents create local-first article infographics, self-contained HTML charts and reports from local structured data, browser-based data decks, chart recommendations, and Miao Vision spec validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Miao Vision to turn article content or local CSV, TSV, XLSX, and JSON files into self-contained visual HTML artifacts, browser-based decks, or validated visualization specs. It is intended for local workflows where the agent can run shell commands and review generated specs before rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local shell commands and may install a miao-viz CLI binary when no compatible CLI is present. <br>
Mitigation: Review the command plan before execution, approve installation only when expected, and rely on the documented checksum verification path for downloaded binaries. <br>
Risk: Article URL fetching can access private or internal URLs if the user supplies them. <br>
Mitigation: Use only URLs intended for local processing and avoid private or internal URLs unless that access is deliberate. <br>
Risk: Local datasets and generated HTML outputs may contain sensitive information in /tmp/miao-vision. <br>
Mitigation: Treat generated files as sensitive when source data is confidential and remove local outputs after use. <br>
Risk: Visualization claims can be misleading if generated specs include unsupported metrics or conclusions. <br>
Mitigation: Validate specs before rendering and keep numeric claims grounded in the available evidence context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill) <br>
- [Miao Vision installation](install/README.md) <br>
- [Article URL / Markdown To Infographic](references/article-infographic.md) <br>
- [Data File To Visualization Report](references/data-report.md) <br>
- [Data File To Browser Deck](references/browser-deck.md) <br>
- [Chart Selection](references/chart-selection.md) <br>
- [Miao Vision VizSpec Reference](references/vizspec.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and visualization specifications that render to self-contained HTML artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated work is local-first and commonly uses /tmp/miao-vision for intermediate specs, evidence contexts, and rendered artifacts.] <br>

## Skill Version(s): <br>
0.1.26 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
