## Description: <br>
Analyzes complex workplace issues to choose the first skill to use and plan skill order, parameter handoffs, stopping conditions, and the final output skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and workflow operators use this skill to decide whether a single skill is enough or whether a short sequence of skills is needed for complex workplace tasks. It is intended for routing, parameter handoff planning, stopping conditions, and final-output skill selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommended skill chains may be used in sensitive business workflows such as pricing, refunds, complaints, or order delivery without sufficient review. <br>
Mitigation: Review the recommended skill chain before acting on it, and confirm that required facts are present before downstream skills are used. <br>
Risk: The routing recommendation could be mistaken for execution authority. <br>
Mitigation: Use the skill as routing guidance only; it should stop when information is missing and should not execute business actions automatically. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-route) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown routing analysis with tables and concise recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes parameter status, problem type, single-skill versus multi-skill judgment, recommended skill chain, parameter handoff guidance, stopping conditions, and final output skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
