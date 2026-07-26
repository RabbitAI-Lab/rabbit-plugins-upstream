## Description: <br>
Analyze Gemini Cloud Billing and usage JSON, show actual Google AI spend in lattes, and estimate how many lattes the user could recover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze local Gemini Cloud Billing and usage JSON, understand actual Gemini spend, and estimate directional recoverable cost in a concise report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Billing and usage JSON may contain sensitive project and spend details. <br>
Mitigation: Use the skill only with local files the user selects, do not upload or reproduce raw billing data, and keep the local-analysis privacy notice visible in the report. <br>
Risk: Estimated recoverable cost may be mistaken for guaranteed savings. <br>
Mitigation: Present recoverable cost as directional, explain the recovery basis, and avoid claims that quality will be preserved without testing. <br>
Risk: The skill ends with an external action link that is outside the local analysis path. <br>
Mitigation: Review the external website separately before entering information there. <br>


## Reference(s): <br>
- [Supported input formats](artifact/references/input-formats.md) <br>
- [ClawHub skill page](https://clawhub.ai/margaretzybgl/skills/take-back-my-latte-from-gemini) <br>
- [Take Back My Latte website](https://take-back-my-latte.margaret-zybgl.chatgpt.site) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with concise text and local Python command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local Python analysis on user-selected JSON files; the report is under 250 words by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
