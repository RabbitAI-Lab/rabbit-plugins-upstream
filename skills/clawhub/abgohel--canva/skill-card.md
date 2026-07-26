## Description: <br>
Create, export, and manage Canva designs via the Canva Connect API, including social posts, carousels, graphics, template autofill, exports, and asset uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abgohel](https://clawhub.ai/user/abgohel) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and design automation users use this skill to authenticate with Canva, list or create designs, export assets, upload files, and automate template-based social media or graphics workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read from and write to the connected Canva account through OAuth scopes and stored tokens. <br>
Mitigation: Use the minimum Canva scopes needed, protect CANVA_CLIENT_SECRET, and keep ~/.canva/tokens.json permissions restrictive. <br>
Risk: Upload commands send the selected local file to Canva. <br>
Mitigation: Confirm exact file paths before upload and avoid selecting sensitive or unintended files. <br>


## Reference(s): <br>
- [Canva ClawHub skill page](https://clawhub.ai/abgohel/skills/canva) <br>
- [Canva Connect API Docs](https://www.canva.dev/docs/connect/) <br>
- [Canva Connect OpenAPI Spec](https://www.canva.dev/sources/connect/api/latest/api.yml) <br>
- [Canva Developers](https://www.canva.com/developers/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented Canva API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CANVA_CLIENT_ID and CANVA_CLIENT_SECRET; Canva OAuth tokens are stored locally in ~/.canva/tokens.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
