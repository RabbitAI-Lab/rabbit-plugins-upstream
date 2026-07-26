## Description: <br>
Snipe-IT (snipeitapp.com). Use this skill for ANY Snipe-IT request: searching and reading data through the OOMOL Snipe-IT connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to search and read Snipe-IT inventory records, including users, hardware assets, categories, companies, status labels, and the current connected user, through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Inventory data exposure <br>
Mitigation: Only install and run the skill when the agent session is allowed to view asset and user records from the connected Snipe-IT account. <br>
Risk: Unexpected write or destructive connector actions <br>
Mitigation: Approve write or destructive connector actions only after reviewing the target, schema-derived payload, and expected effect. <br>
Risk: Incorrect connector payloads <br>
Mitigation: Fetch the live action schema with `oo connector schema` before constructing and running an action payload. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-snipe-it) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Snipe-IT Homepage](https://snipeitapp.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions return JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
