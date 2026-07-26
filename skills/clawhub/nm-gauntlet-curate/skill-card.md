## Description: <br>
Adds developer-authored annotations to the gauntlet knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to capture tribal knowledge, rationale, and module-specific context as local gauntlet annotations for future review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive or private information could be saved into local gauntlet annotation files. <br>
Mitigation: Review annotation content before saving and exclude credentials, customer data, private incident details, and sensitive internal strategy. <br>
Risk: Incorrect or incomplete rationale could make future gauntlet knowledge-base guidance misleading. <br>
Mitigation: Confirm the module, concept, and rationale before saving the YAML annotation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-curate) <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration] <br>
**Output Format:** [YAML annotation file with brief confirmation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes annotations under .gauntlet/annotations/<slug>.yaml when the agent is allowed to save files.] <br>

## Skill Version(s): <br>
1.9.16 (source: release metadata; SKILL.md frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
