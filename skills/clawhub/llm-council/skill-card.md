## Description: <br>
Use when the user asks for a council, second opinions, a debate, or multi-perspective deliberation on a question, or when a decision is high-stakes, contested, or ambiguous enough that a single answer risks being confidently wrong or sycophantic. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ddanninger](https://clawhub.ai/user/ddanninger) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to obtain structured multi-perspective deliberation for high-stakes, ambiguous, or contested questions. It is intended to surface disagreement, critique user-stated preferences, and synthesize a final verdict with confidence, dissent, and concrete falsifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend extra time and model calls by dispatching multiple advisors and reviewers. <br>
Mitigation: Use it for genuinely high-stakes, ambiguous, or contested decisions rather than routine questions. <br>
Risk: Multi-agent deliberation can still produce incorrect or misleading guidance even when dissent is preserved. <br>
Mitigation: Review the verdict, dissent, confidence, flip conditions, and falsifier before acting on consequential recommendations. <br>


## Reference(s): <br>
- [LLM Council skill page](https://clawhub.ai/ddanninger/skills/llm-council) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final output includes a verdict, vote tally, endorsement split when applicable, consensus, dissent, flip conditions, and one concrete falsifier.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
