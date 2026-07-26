## Description: <br>
Kintone connector skill for searching and reading Kintone account data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Kintone connector schemas and read user, department, group, and service assignments from an OOMOL-connected Kintone account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connecting Kintone through this skill allows OOMOL-mediated read access to Kintone user and organization metadata. <br>
Mitigation: Use the skill only when that connection is acceptable, and keep routine execution to the listed read actions. <br>
Risk: First-time setup may require installing the oo CLI from an external installer. <br>
Mitigation: Verify the oo CLI installer before setup and run auth or connection steps only after the matching command failure. <br>
Risk: Future connector schemas could expose write or destructive Kintone actions. <br>
Mitigation: Inspect the live action schema and require explicit user confirmation before any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub Kintone skill page](https://clawhub.ai/oomol/skills/oo-kintone) <br>
- [Kintone homepage](https://www.kintone.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown text with oo CLI shell commands and JSON connector payloads or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses read-oriented Kintone connector actions; live schemas should be inspected before payload construction.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
