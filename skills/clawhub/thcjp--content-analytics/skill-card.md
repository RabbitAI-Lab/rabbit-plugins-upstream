## Description:

Analyzes content performance by calculating views, completion, engagement, conversion, and sharing metrics, assigning S/A/B/C ratings, producing optimization suggestions, and supporting a six-step publish-to-learn feedback loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze post-publication content performance, generate ratings and recommendations, identify evergreen content, optimize posting times, and run a closed-loop workflow that feeds lessons into future content generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify PostgreSQL analytics and publishing tables.

Mitigation: Install it only where table writes are approved, use least-privilege database credentials, and review write access before enabling scheduled or full-loop runs.

Risk: The closed-loop workflow can perform cross-tenant synchronization and read tenant publishing records.

Mitigation: Confirm tenant isolation and require an explicit tenant context for operational use.

Risk: The skill may run Docker, opencli, and Python subprocesses.

Mitigation: Run it in a controlled agent environment with approved binaries and review subprocess permissions before installation.

Risk: The learning step can persist derived performance lessons for later content generation.

Mitigation: Confirm whether learned performance data may be retained and reused before enabling the learn step.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/content-analytics)
- [Publisher Profile](https://clawhub.ai/user/thcjp)
- [Business Rules](references/business_rules.md)
- [Error Codes](references/error_codes.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON responses and Markdown guidance with Python command execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and data-copilot MCP configuration via DATA_COPILOT_MCP_URL.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
