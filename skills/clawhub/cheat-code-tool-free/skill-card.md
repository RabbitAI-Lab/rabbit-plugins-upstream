## Description:

能力扩展工具免费版 helps an AI agent query external structured knowledge for current technical documentation, API specifications, and domain knowledge when its training data may be incomplete or stale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to let an agent request external technical knowledge, especially for recent framework behavior, standards comparisons, and implementation guidance outside the model's training data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command execution authority for a knowledge lookup workflow.

Mitigation: Install with the minimum permissions needed for the intended workflow, and deny local file or command execution unless those capabilities are explicitly required and constrained.

Risk: External knowledge queries can expose secrets, proprietary code, or sensitive prompts to a third-party service.

Mitigation: Use the skill only for explicit technical lookups and remove credentials, proprietary code, and confidential data before sending queries.

Risk: Returned external knowledge may be stale, incomplete, or inconsistent with authoritative sources.

Mitigation: Review the returned information, prefer cited authoritative sources, and verify critical technical or security decisions before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cheat-code-tool-free)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON examples with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide external API queries and returns structured result text with execution metadata in examples.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
