## Description: <br>
Helps agents identify gain, loss, attribute, and goal framing in decisions or communication, construct equivalent alternative frames, and produce a frame-independent audit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agent developers use this skill to test whether a decision, statistic, or persuasive message changes meaning when restated in equivalent gain, loss, attribute, or goal frames. It is useful for decision review, communication review, and spotting one-sided or manipulative framing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can be used for persuasion and may support misleading omissions or manipulative framing in high-stakes contexts. <br>
Mitigation: Present equivalent alternative frames, avoid hiding material facts, and use extra review for medical, financial, legal, political, or other high-stakes decisions. <br>
Risk: A framed option may be treated as neutral when the wording is steering the decision. <br>
Mitigation: Require the audit to identify the active frame, construct a mathematically equivalent alternative, and check whether the decision changes across frames. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/framing-effect) <br>
- [Primary sources](references/sources.md) <br>
- [Tversky and Kahneman Asian Disease example](examples/tversky-and-kahnemans-1981-asian-disease-study.md) <br>
- [AI capex framing example](examples/ai-capex-visionary-investment-vs-bubble-overbuild-2024-2026.md) <br>
- [deciqAI framing effect page](https://www.deciqai.com/c/framing-effect) <br>
- [Machine-readable skill metadata](https://www.deciqai.com/s/framing-effect.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown framing audit with concise prose and structured decision fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step coaching questions before producing the audit when the user is unfamiliar with the concept.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
