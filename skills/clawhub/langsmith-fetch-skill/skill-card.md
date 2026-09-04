## Description:

Debug LangChain and LangGraph agents by fetching LangSmith Studio execution traces to inspect errors, tool calls, memory operations, and performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to debug LangChain and LangGraph agents by fetching recent LangSmith traces, investigating failures, reviewing tool calls, checking memory operations, and analyzing performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private LangSmith trace data for the configured project.

Mitigation: Install only when the langsmith-fetch CLI is trusted, use scoped LangSmith credentials, and limit use to intended projects.

Risk: Exported debug sessions or JSON traces may contain prompts, tool outputs, memory data, and conversation traces.

Mitigation: Treat exported folders and trace files as sensitive and avoid sharing or logging them in public or untrusted locations.

Risk: LangSmith API keys may be exposed if printed into shared terminals or logs.

Mitigation: Avoid echoing API keys in shared environments and prefer scoped credentials.

## Reference(s):

- [Server-resolved source repository](https://github.com/OthmanAdi/langsmith-fetch-skill)
- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/langsmith-fetch-skill)
- [LangSmith Fetch CLI](https://github.com/langchain-ai/langsmith-fetch)
- [LangSmith Studio](https://smith.langchain.com/)
- [LangChain Docs](https://docs.langchain.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON or exported trace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local debug-session folders or JSON trace exports when the user requests export or deep analysis.]

## Skill Version(s):

0.1.0 (source: changelog, released 2025-12-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
