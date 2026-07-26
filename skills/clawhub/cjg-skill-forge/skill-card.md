## Description: <br>
Skill Forge is a meta-skill for creating, upgrading, reviewing, and consolidating WorkBuddy skills using feedback loops, coverage audits, external benchmarking, validation, and a weighted review rubric. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use Skill Forge to create or upgrade skills, audit whether a skill meets quality targets, and plan consolidation of overlapping local skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Default local feedback logs and anonymous cloud feedback uploads may be unsuitable for users who do not want usage signals recorded or sent to bundled endpoints. <br>
Mitigation: Review the install notice and use the documented opt-outs before relying on the skill when local logging or cloud upload is not acceptable. <br>
Risk: Publishing and proposal commands can read local credentials and change or publish skill packages. <br>
Mitigation: Treat those commands as privileged actions; review command arguments, credential locations, and package contents before execution. <br>
Risk: Semantic recast scanning can send skill metadata to a configured embedding service when semantic mode is enabled. <br>
Mitigation: Use the default non-semantic scan unless external metadata processing is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Forge release page](https://clawhub.ai/j-levee/skills/cjg-skill-forge) <br>
- [Anti-Patterns](references/anti-patterns.md) <br>
- [Churn Reflector](references/churn-reflector.md) <br>
- [Real-Machine Forge](references/contest-hard-forge.md) <br>
- [Coverage Audit](references/coverage-audit.md) <br>
- [Coverage Seeding Rules](references/coverage-seeding.md) <br>
- [Feedback Loop](references/feedback-loop.md) <br>
- [Persona Skill Design](references/persona-design.md) <br>
- [Project Governance](references/project-governance.md) <br>
- [Quality Iteration Playbook](references/quality-iteration-playbook.md) <br>
- [Simulation Testing](references/simulation-testing.md) <br>
- [Skill Consolidation](references/skill-consolidation.md) <br>
- [Skill Review Rubric](references/skill-review-rubric.md) <br>
- [Skill Types](references/skill-types.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with checklists, scores, code snippets, shell commands, and JSON or configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce skill drafts, review scores, audit reports, recast plans, and publishing guidance.] <br>

## Skill Version(s): <br>
2.9.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
