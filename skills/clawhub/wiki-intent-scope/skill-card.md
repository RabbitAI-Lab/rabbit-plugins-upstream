## Description: <br>
Wiki Intent Scope converts free-form client research requests into structured Wiki research scoping outputs, including research-object normalization, intent classification, assumptions, confirmation items, scope.md, and scope.json. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leadleo](https://clawhub.ai/user/leadleo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Research and consulting teams use this skill at project kickoff to turn client statements into a structured research task definition, including the likely decision context, research intent, scope boundaries, assumptions, and items needing human confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat scoping assumptions as final business, legal, compliance, policy, or research recommendations. <br>
Mitigation: Keep sensitive decisions under human review and use the output as a task-scoping handoff rather than a final recommendation. <br>
Risk: Broad triggers for ranking, public communication, or brand-positioning requests may influence sensitive claims if the output is not reviewed. <br>
Mitigation: Confirm the skill is being used for scope definition, verify public-claim and evidence requirements manually, and review outputs before relying on them. <br>


## Reference(s): <br>
- [Intent Taxonomy](references/intent_taxonomy.md) <br>
- [Output Contract](references/output_contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Chinese chat summary plus scope.md and scope.json] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces scoping assumptions, confirmation items, risk notes, and stable handoff fields for downstream Wiki research workflow steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
