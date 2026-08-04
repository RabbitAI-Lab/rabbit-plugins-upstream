## Description: <br>
Routes complex workplace requests to the appropriate skill or skill sequence, including parameter handoff, stop conditions, and final output ownership across customer, quotation, order, support, collaboration, market, and business intelligence workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and business operators use this skill to decide whether a request needs one skill or a staged skill chain, what context to pass forward, and when to stop for missing or conflicting information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may recommend downstream workflow or research skills that perform market research, customer monitoring, or external communication. <br>
Mitigation: Review any downstream skill separately before use, especially skills that access current customer or market information or prepare external messages. <br>
Risk: Missing or conflicting context can lead to an inappropriate skill chain or premature escalation of weak business signals. <br>
Mitigation: Apply the documented stop conditions before continuing: require a clear subject, source, timeframe, goal, and minimum inputs, and keep unverified facts marked as unverified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-route) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown with routing conclusions, parameter status tables, skill-chain tables, handoff notes, stop conditions, and final-output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces recommendations and stopping guidance; it does not execute downstream skills by itself.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
