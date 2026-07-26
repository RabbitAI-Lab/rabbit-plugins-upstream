## Description: <br>
Provides Chinese-language guidance for designing AI agent test plans that cover functionality, safety, controllability, reliability, hallucination checks, reasoning validation, and tool-call behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and AI safety reviewers use this skill to create structured test plans and test cases for AI agents, chatbots, and assistants. It helps evaluate reasoning behavior, tool invocation, prompt-injection resistance, hallucination risk, role boundaries, memory consistency, and human-control safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad AI-assistant-related phrases and produce testing guidance when the user's intent is ambiguous. <br>
Mitigation: Confirm the target agent, scope, and testing objective before applying the generated plan. <br>
Risk: The artifact declares Bash and WebFetch tool access, which can affect local projects or fetch external content if allowed by the host agent. <br>
Mitigation: Review proposed shell commands and web fetches before execution, and run tests in a controlled environment. <br>
Risk: Generated test plans and safety audit suggestions may miss product-specific controls or overstate coverage. <br>
Mitigation: Map each test case to product requirements, risk assessments, and human review before release decisions. <br>


## Reference(s): <br>
- [Agent nine-dimension test framework](references/test-framework.md) <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-agent-testing) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Analysis] <br>
**Output Format:** [Markdown with structured test plans, test cases, checklists, and risk notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include requirement traceability IDs, tool-call test cases, hallucination checks, safety audit items, and reasoning validation guidance.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
