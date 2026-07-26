## Description: <br>
Identifies testing areas that may look simple but carry high risk, then helps prioritize limited QA resources with risk levels and mitigation suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, test leads, and development teams use this skill to triage test focus when time is limited, requirements are changing, or a feature may hide business, data, integration, or technical risk. It produces prioritized risk areas, a probability-impact matrix, and mitigation suggestions for test planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may frame broad testing requests through a risk-assessment lens even when the user needs a general test plan. <br>
Mitigation: Use it when risk prioritization is desired, and choose a general test-planning skill when the goal is comprehensive test design. <br>
Risk: A risk assessment can miss high-risk areas if the requirements or scenario tree are incomplete. <br>
Mitigation: Supplement the requirement decomposition and scenario context, then rerun the risk assessment before relying on the priority list. <br>


## Reference(s): <br>
- [Risk Signals Radar and Checklist](references/risk-signals.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown risk assessment report with risk matrix tables and mitigation suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each risk point is expected to include a unique risk ID and a linked requirement ID.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
