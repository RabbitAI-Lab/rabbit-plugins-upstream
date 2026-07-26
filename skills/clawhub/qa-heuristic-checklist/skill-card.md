## Description: <br>
Provides reusable QA heuristic checklist templates for common feature types such as forms, lists, shopping carts, payments, imports and exports, approvals, notifications, and permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and test leads use this skill to identify the right checklist for a feature type and avoid missing common test areas, especially when starting test design for an unfamiliar feature. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad testing-related prompts where a deeper QA strategy skill would be more appropriate. <br>
Mitigation: Use this skill for checklist coverage, and choose a more specific QA skill for scenario design, boundary analysis, or deeper test strategy. <br>
Risk: Example checklist items may describe destructive test actions such as deleting cart items or changing permissions. <br>
Mitigation: Treat those items as test design prompts and execute them only in appropriate test environments with review of affected data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-heuristic-checklist) <br>
- [Functional heuristic checklists](references/checklists.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown checklist guidance with covered areas, uncovered areas, and exploration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should mark covered heuristic areas and avoid creating new unique traceability IDs.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
