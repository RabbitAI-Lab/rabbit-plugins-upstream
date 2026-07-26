## Description: <br>
Qa Release Risk Governance helps agents assess software release risk, plan gray or canary rollout strategies, prepare rollback plans, and define production monitoring before release decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, release managers, and DevOps teams use this skill to evaluate release readiness, identify blocking issues, choose a rollout strategy, and plan rollback and monitoring coverage. It is decision-support for release planning, not an automation tool for deployment or rollback execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Release, rollback, production configuration, and data-migration recommendations may affect high-impact operational decisions if treated as approval to act. <br>
Mitigation: Keep human approval and normal change-management controls around actual deployment, rollback, production configuration, and data-migration actions. <br>
Risk: The generated release assessment can be mistaken for an executable release or rollback action. <br>
Mitigation: Use the skill output as planning guidance only; verify approval authority, rollout percentages, rollback steps, and monitoring thresholds before taking operational action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-release-risk-governance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown release risk assessment and rollout plan] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes traceability IDs in the REL-XXXX format, release decision guidance, risk summary, blocking issues, rollback plan, and monitoring recommendations.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
