## Description: <br>
Helps an agent slow down confident decisions by testing claims against falsification criteria, counter-evidence, ambiguous evidence, and structured review triggers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and decision-support agents use this skill when a team or individual is converging on a claim without actively seeking disconfirming evidence. It guides the agent to state the claim, define falsification tests, audit evidence-seeking, re-read ambiguous evidence, install a structural countermeasure, and set update conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat old or external reference links as current factual authority. <br>
Mitigation: Review linked external references for currency before relying on them for live factual claims. <br>
Risk: The skill may slow decisions by introducing structured follow-up questions and wait points. <br>
Mitigation: Use it for decisions where the value of disconfirmation justifies the added review effort. <br>
Risk: The skill can surface counter-evidence and uncertainty but cannot determine truth on its own. <br>
Mitigation: Pair its output with domain review, source checks, and a named owner for final decision accountability. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/confirmation-bias) <br>
- [Publisher profile](https://clawhub.ai/user/deciqai) <br>
- [Confirmation Bias runtime page](https://www.deciqai.com/c/confirmation-bias) <br>
- [Machine-readable metadata](https://www.deciqai.com/s/confirmation-bias.json) <br>
- [Knowledge skills repository](https://github.com/deciqAI/knowledge-skills) <br>
- [Primary sources](references/sources.md) <br>
- [Peter Wason's 2-4-6 Task, 1960](examples/peter-wasons-2-4-6-task-1960.md) <br>
- [The FBI Mayfield Fingerprint Misidentification, 2004](examples/2004-fbi-mayfield-fingerprint-misidentification.md) <br>
- [The AI Thesis War (2023-2026)](examples/ai-thesis-confirmation-2023-2026.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance and structured text templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may ask step-by-step follow-up questions and stop at explicit wait points when coaching a user.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
