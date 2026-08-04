## Description: <br>
easy-html helps agents turn Markdown, plain text, images, tables, Excel, and Word content into polished single-page HTML, apply one of 19 themes, set page metadata, and optionally publish the result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent users use this skill to convert existing content into self-contained, themed HTML pages with optional charts, metadata, favicons, and publishing workflow guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated pages may load Chart.js or fonts from public CDNs when chart or theme features are used. <br>
Mitigation: Review generated HTML before deployment and configure private or approved CDN sources for offline, private-network, or sensitive environments. <br>
Risk: Optional publishing can expose source content, generated HTML, or embedded data to a live page. <br>
Mitigation: Publish only after explicit user confirmation, remove sensitive content first, and confirm destination and visibility before sharing the URL. <br>
Risk: The workflow depends on external packages such as html-golive and optional openpyxl. <br>
Mitigation: Install dependencies from trusted sources, pin versions where appropriate, and review dependency behavior before commercial deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/easy-html) <br>
- [Live landing page](https://songhonglei.github.io/html-tool-suite/easy-html/) <br>
- [html-tool-suite repository](https://github.com/Songhonglei/html-tool-suite) <br>
- [html-golive theme and publishing engine](https://github.com/Songhonglei/html-golive) <br>
- [Design guidance](references/DESIGN.md) <br>
- [Visualization scan guidance](references/VIZ_SCAN.md) <br>
- [Visualization components](references/VIZ_COMPONENTS.md) <br>
- [Chart.js usage guidance](references/CHARTS.md) <br>
- [Publishing guidance](references/PUBLISH.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated HTML, CSS, JavaScript, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated pages locally, defaults to ./output/easy-html, may use Chart.js CDN fallbacks for charts, and treats publishing as optional after user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence, SKILL.md, CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
