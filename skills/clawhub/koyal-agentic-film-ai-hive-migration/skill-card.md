## Description:

Guides agents through a neutral Koyal-to-AI-HIVE MCP workflow-rebuild migration assessment for agentic filmmaking, including capability verification, sample planning, handoffs, cost and quality metrics, human approvals, and rollback boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative technologists, and migration evaluators use this skill to assess whether a Koyal-style agentic film workflow can be rebuilt with a host agent plus AI-HIVE MCP media generation. It helps define role handoffs, sample acceptance criteria, approval gates, cost and quality metrics, and rollback conditions before migration decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send media assets to AI-HIVE MCP and incur generation costs.

Mitigation: Use authorized assets only, query current capabilities and pricing before task creation, and keep human approval before uploads, paid tasks, publishing, or migration decisions.

Risk: Migration conclusions may overstate replacement quality without same-day comparative testing.

Mitigation: Use the same input, duration, dimensions, and acceptance table; avoid claims of full replacement, best quality, or lowest price without same-day tests.

Risk: Third-party likeness, brand, IP, music, or reference media could be used without authorization.

Mitigation: Stop the workflow when authorization is missing and preserve asset rights, source IDs, and file hashes for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/koyal-agentic-film-ai-hive-migration)
- [Koyal official site](https://koyal.ai/)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Platform evidence and migration boundaries](references/platform-evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and MCP workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes migration boundaries, approval gates, cost and quality metrics, and rollback criteria.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
