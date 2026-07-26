## Description: <br>
Zixflow (zixflow.com). Use this skill for ANY Zixflow request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent read, create, update, query, and delete Zixflow workspace records, lists, and members through the OOMOL oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete Zixflow data. <br>
Mitigation: Use a least-privilege Zixflow token where possible, and explicitly review prompts and payloads before allowing write or destructive actions. <br>
Risk: Incorrect query or record payloads could affect the wrong workspace data. <br>
Mitigation: Inspect the live connector schema before building each payload and confirm the intended target for write or destructive operations. <br>


## Reference(s): <br>
- [Zixflow homepage](https://zixflow.com) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zixflow) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Zixflow connector schemas before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
