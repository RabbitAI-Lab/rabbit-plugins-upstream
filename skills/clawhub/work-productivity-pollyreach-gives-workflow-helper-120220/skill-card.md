## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn PollyReach-style workflow demand into practical plans, checklists, analyses, code changes, and verification notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to clarify workflow requirements, create local-hardware-friendly implementation plans, produce reusable checklists or artifacts, and verify the result against stated success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on unrelated productivity, phone, or number-related requests because its trigger terms are broad. <br>
Mitigation: Narrow the trigger keywords and review implicit invocation behavior before relying on automatic routing. <br>
Risk: Workflow guidance can be incomplete or mismatched if the user's desired outcome, constraints, or success criteria are unclear. <br>
Mitigation: Restate the goal and assumptions, ask only for materially missing information, and include a verification note with remaining risks. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-pollyreach-gives-workflow-helper-120220) <br>
- [PollyReach Demand Signal](https://clawhub.ai/skills/pollyreach) <br>
- [Ask HN: AI Over-Reliance Workflow Signal](https://news.ycombinator.com/item?id=48979474) <br>
- [V2EX UX Comparison Signal](https://www.v2ex.com/t/1228874) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, limits, validation steps, and remaining risks when relevant.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
