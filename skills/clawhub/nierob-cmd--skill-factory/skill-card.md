## Description: <br>
Scaffolds a router plus 2-6 variant skills for a problem with several recognizable variants, including eval-tuned triggers, progressive disclosure, and a build checklist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nierob-cmd](https://clawhub.ai/user/nierob-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create a small family of related agent skills: one deterministic router and two to six self-contained variant skills for problems whose variants can be recognized up front. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated router and variant skill files can affect future agent behavior if their routing rules or instructions are wrong. <br>
Mitigation: Review the generated skill files, routing table, recognition rules, and variant checklists before installing or relying on them. <br>
Risk: A skill family with unclear variant boundaries can route tasks to the wrong variant or produce confusing instructions. <br>
Mitigation: Use hard upfront signals for routing and keep each variant self-contained, as described in the artifact guidance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nierob-cmd/skills/skill-factory) <br>
- [Skill Mechanics Reference](references/skill-mechanics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with skill file content, routing tables, checklists, and optional shell commands for packaging or evaluation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces proposed router and variant skill structures that should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
