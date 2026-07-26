## Description: <br>
Helps an agent analyze claims drawn from visible winners, surviving investments, successful companies, or other survivor-filtered samples by identifying the missing non-survivor population and marking conclusions as conditional unless corrected. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to make reasoning about success stories, investment performance, startup outcomes, medical outcomes, career advice, and historical examples more selection-aware. It guides the agent to state the claim, identify the survival filter, construct a non-survivor hypothesis, and either correct the inference or mark it as conditional. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real user examples or case details could be retained in the skill after use. <br>
Mitigation: Do not store user examples in the skill unless the user explicitly agrees and the content is sanitized. <br>
Risk: The skill can still produce misleading conclusions if the agent treats survivor-only evidence as population evidence. <br>
Mitigation: Review the analysis for an identified survival filter, a non-survivor hypothesis, and a conclusion that is corrected or clearly marked as conditional. <br>


## Reference(s): <br>
- [Survivorship Bias on ClawHub](https://clawhub.ai/deciqai/skills/survivorship-bias) <br>
- [Primary Sources](references/sources.md) <br>
- [Abraham Wald and the Statistical Research Group, 1943](examples/abraham-wald-and-the-statistical-research-group-1943.md) <br>
- [Mutual Fund Survivorship and Reported Returns, 1971-1996](examples/mutual-fund-survivorship-and-reported-returns-1996.md) <br>
- [AI-Startup Survivorship, 2023-2026](examples/ai-startup-survivorship-2023-2026.md) <br>
- [deciqAI Survivorship Bias Page](https://www.deciqai.com/c/survivorship-bias) <br>
- [Machine-Readable Skill Metadata](https://www.deciqai.com/s/survivorship-bias.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis template with concise reasoning steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces structured claim, survival-filter, non-survivor hypothesis, and corrected-inference sections; no executable code or shell commands.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
