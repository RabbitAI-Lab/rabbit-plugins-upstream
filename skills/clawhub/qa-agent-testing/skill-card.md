## Description:

Helps QA teams design nine-dimension test plans for AI agents, covering functionality, safety, controllability, reliability, hallucination, reasoning, and tool-call behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to scope and produce AI agent test plans, test cases, checklists, and safety audits. It is intended for evaluating agent behavior across functional, safety, reliability, reasoning, hallucination, and tool-use dimensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be mistaken for an execution harness rather than a QA planning framework.

Mitigation: Treat generated plans, cases, and audits as reviewable QA guidance and validate results through the user's test process.

Risk: Broad trigger phrases about AI assistants or chatbots may activate the skill when the user is not asking for testing.

Mitigation: Clarify testing intent before applying the framework to general assistant or chatbot discussions.

Risk: The skill recommends installing a larger external QA skill set for the full workflow.

Mitigation: Review the external package and install only when the broader QA workflow is intentionally needed.

## Reference(s):

- [Agent 九维测试框架](references/test-framework.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-agent-testing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test plans, test cases, checklists, and audit notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes traceability IDs, priority levels, coverage notes, and risk levels when generating test cases.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter reports 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
