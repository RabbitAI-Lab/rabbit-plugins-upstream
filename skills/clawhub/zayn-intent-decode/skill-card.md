## Description: <br>
分析客户原话和上下文，区分明确表达、核心关注点、可能意图和仍需确认的信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer-facing teams and operators use this skill to analyze customer statements and context, separating explicit statements, core concerns, possible intent, alternative explanations, and questions that still need confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer conversation context may include sensitive personal, customer, or business information. <br>
Mitigation: Provide only the minimum necessary context, redact sensitive details where possible, and avoid entering unnecessary confidential information. <br>
Risk: Intent analysis can overstate inferred customer motivations when evidence is incomplete. <br>
Mitigation: Keep explicit statements separate from possible intent, label low-evidence interpretations, and ask clarifying questions before treating an interpretation as fact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-intent-decode) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown analysis with parameter status, explicit customer statements, possible intent, alternative interpretations, clarification questions, and confidence.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only; no code, tools, persistence, or credential use.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence; artifact docs note v0.1 draft content) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
