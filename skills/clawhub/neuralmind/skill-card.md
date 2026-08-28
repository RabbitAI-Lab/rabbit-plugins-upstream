## Description:

Answer questions about a code repository in ~800 tokens instead of loading 50,000+ tokens of raw source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dfrostar](https://clawhub.ai/user/dfrostar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use NeuralMind to navigate unfamiliar repositories, answer codebase questions, locate definitions, trace callers, inspect file structure, and retrieve compact project context before reading source directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local repository indexes and learned associations may persist project context beyond a single agent session.

Mitigation: Install only for repositories where persistent .neuralmind data is acceptable, and use project isolation or the documented synapse toggles when recall or export should be disabled.

Risk: Broad code-question triggers can encourage agents to rely on retrieved summaries without checking source when detail matters.

Mitigation: Use retrieved context to locate relevant code, then read source directly when implementation details, security behavior, or exact changes must be verified.

## Reference(s):

- [NeuralMind ClawHub listing](https://clawhub.ai/dfrostar/skills/neuralmind)
- [dfrostar ClawHub profile](https://clawhub.ai/user/dfrostar)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to retrieve compact JSON or markdown context from NeuralMind tools, including learned project associations when enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
