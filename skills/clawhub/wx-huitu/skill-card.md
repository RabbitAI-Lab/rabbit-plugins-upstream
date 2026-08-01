## Description: <br>
Wx Huitu helps agents turn WeChat article text or data descriptions into PNG chart packages by profiling the data, recommending one of 18 chart layouts, generating HTML, and capturing screenshots with Puppeteer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content teams, analysts, and agents preparing WeChat articles use this skill to convert article data or structured data descriptions into publication-ready static chart images. It is suited for generating local PNG chart packages with explicit review points for chart choice and optional cloud sync. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated charts may contain article source data and can be uploaded to Feishu if cloud sync is requested. <br>
Mitigation: Keep cloud sync off by default and upload only after explicit user confirmation; allow the user to skip cloud sync. <br>
Risk: The skill writes local PNG files and runs Puppeteer or Chrome to render screenshots. <br>
Mitigation: Review output paths and browser commands before execution, and run the skill only in an environment where local file writes and browser automation are expected. <br>
Risk: Rendering may make network requests to load external fonts. <br>
Mitigation: Use the skill only when external font fetching is acceptable, or replace external fonts with local or system fonts before rendering. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/wx-huitu) <br>
- [Workflow reference](references/workflow.md) <br>
- [Chart system reference](references/chart-system.md) <br>
- [Design tokens reference](references/design-tokens.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance plus generated HTML/CSS/SVG and PNG image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PNG charts are saved locally; optional Feishu cloud upload requires explicit user confirmation.] <br>

## Skill Version(s): <br>
2.2.0 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
