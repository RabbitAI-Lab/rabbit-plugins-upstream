## Description: <br>
Lanhu Design helps agents inspect Lanhu UI design drafts, extract HTML/CSS specs and design tokens, retrieve slices and assets, and implement UI from Lanhu handoff data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oyjt](https://clawhub.ai/user/oyjt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to work from Lanhu UI design projects: list designs, download design images, extract specs and assets, and generate implementation guidance or code while preserving design fidelity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a full Lanhu browser session cookie through LANHU_COOKIE. <br>
Mitigation: Use a dedicated low-privilege Lanhu account where possible, keep the cookie out of shell history, logs, and version control, and rotate it after use. <br>
Risk: The skill can download design images and slices into local project directories. <br>
Mitigation: Review output paths and target asset directories before running download commands. <br>
Risk: Authentication failures or expired cookies can cause partial workflows or failed API calls. <br>
Mitigation: Stop after HTTP 401 or 403 errors, refresh LANHU_COOKIE, and rerun the workflow from the design listing step. <br>


## Reference(s): <br>
- [Lanhu design tools reference](artifact/references/lanhu-design-tools.md) <br>
- [Design implementation rules](artifact/references/design-implementation-rules.md) <br>
- [Server-resolved source import](https://github.com/oyjt/lanhu-design/tree/main/skills/lanhu-design) <br>
- [ClawHub skill page](https://clawhub.ai/oyjt/skills/lanhu-design) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, HTML, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON, HTML, code, configuration notes, and downloaded asset files from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js >= 18 and a LANHU_COOKIE environment variable for Lanhu API access.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
