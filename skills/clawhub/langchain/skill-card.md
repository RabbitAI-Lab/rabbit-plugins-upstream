## Description: <br>
Builds and debugs Python LangChain apps, including LCEL chains, agents, tools, retrievers, streaming, structured output, LangGraph state, checkpointers, and middleware. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to write, review, debug, migrate, test, and harden Python LangChain applications. It is especially useful for diagnosing prompt-variable errors, agent loops, tool-call failures, streaming issues, retrieval mistakes, structured-output failures, tracing gaps, retry behavior, rate limits, token cost, and upgrade breaks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored LangChain preferences and memory under ~/Clawic/data/langchain/ can persist across sessions and influence future guidance. <br>
Mitigation: Review or delete ~/Clawic/data/langchain/ to reset the skill memory, and do not store API keys, credentials, or customer data there. <br>
Risk: Generated guidance, code, shell commands, or configuration may be incorrect for a specific LangChain version, provider, deployment, or security posture. <br>
Mitigation: Review generated changes before applying them, pin and test LangChain packages together, and run the recommended deterministic tests, security checks, and deployment gates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/langchain) <br>
- [LangChain skill homepage](https://clawic.com/skills/langchain) <br>
- [Skill overview](artifact/SKILL.md) <br>
- [Setup and preference memory](artifact/setup.md) <br>
- [Security guidance](artifact/security.md) <br>
- [Production guidance](artifact/production.md) <br>
- [Testing guidance](artifact/testing.md) <br>
- [Migration guidance](artifact/migration.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May adapt examples and recommendations from user preferences stored under ~/Clawic/data/langchain/.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
