## Description: <br>
Guides QA and engineering teams through shift-left testing activities across requirements, design, and development to produce early testing checklists, quality gates, and intervention records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and project teams use this skill during requirements, design, and active development to plan shift-left testing, assess testability, define early quality gates, and document phased intervention activities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill during unrelated QA conversations. <br>
Mitigation: Use explicit invocation or narrow trigger wording when installing it in contexts with many QA skills. <br>
Risk: The skill declares Bash access even though the artifact is primarily a document-review and planning aid. <br>
Mitigation: Avoid granting Bash unless the operating environment needs it; use read-only document review for checklist generation where possible. <br>
Risk: Shift-left recommendations can become misleading if source requirements, timelines, or quality targets are incomplete. <br>
Mitigation: Review generated checklists and quality gates with product, engineering, and QA owners before treating them as project controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-shift-left) <br>
- [Publisher profile](https://clawhub.ai/user/kokxi) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown checklists and structured planning notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes traceability to requirements review IDs when available.] <br>

## Skill Version(s): <br>
1.6.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
