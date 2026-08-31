## Description:

Generates AI agent QA plans and test artifacts covering functional behavior, tool use, hallucination checks, prompt injection defenses, control boundaries, reliability, and reasoning validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and agent evaluators use this skill to design structured tests for AI agents, chatbots, and assistants. It helps produce test plans, case tables, safety checks, tool-call tests, hallucination checks, and reasoning validation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may invoke the skill during general AI agent, chatbot, LLM testing, hallucination, prompt injection, or AI security audit discussions.

Mitigation: Review activation behavior in the target agent environment and narrow invocation routing if accidental use would disrupt normal QA workflows.

Risk: The skill can generate security and tool-use test scenarios that may involve real systems, private data, or destructive operations if executed without review.

Mitigation: Treat generated tests as plans until approved, run them in sandboxed or non-production environments, and require human supervision for tests involving live tools, production systems, private data, or destructive actions.

## Reference(s):

- [Agent nine-dimension test framework](references/test-framework.md)
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-agent-testing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test plans, checklists, case tables, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs commonly include agent type classification, required test dimensions, representative test cases, safety and controllability review items, and risk notes.]

## Skill Version(s):

1.7.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
