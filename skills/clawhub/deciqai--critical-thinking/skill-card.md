## Description: <br>
Critical Thinking helps an agent evaluate high-stakes claims by testing competing hypotheses against evidence with an Analysis of Competing Hypotheses matrix. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to evaluate factual claims, AI capability assertions, business decisions, investigations, and other high-stakes conclusions where multiple explanations fit the evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be used in high-stakes evaluation scenarios where an agent's analysis could be mistaken or over-weighted. <br>
Mitigation: Keep final judgment and any real-world action under explicit human control, and treat the ACH output as a reasoning aid rather than an authority. <br>
Risk: A user may start from a vague claim or values-only question where the ACH method is a poor fit. <br>
Mitigation: Use the skill's fit check and coaching mode to elicit a specific factual claim before running the matrix, or redirect when the decision is values-based. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/critical-thinking) <br>
- [Primary sources](references/sources.md) <br>
- [Psychology of Intelligence Analysis](https://www.cia.gov/static/9a5f1162fd0932c29bfed1c030edf4ae/Pyschology-of-Intelligence-Analysis.pdf) <br>
- [NIE 85-3-62 declassified record](https://nsarchive2.gwu.edu/NSAEBB/NSAEBB395/) <br>
- [GSM-Symbolic paper](https://arxiv.org/abs/2410.05229) <br>
- [FrontierMath](https://epoch.ai/frontiermath) <br>
- [deciqAI critical-thinking metadata](https://www.deciqai.com/s/critical-thinking.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured ACH matrices, hypotheses, evidence ratings, assumptions, alternatives, and milestones] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Interactive coaching mode may ask one question at a time before producing the analysis.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
