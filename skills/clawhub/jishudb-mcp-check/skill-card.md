## Description:

Runs explicitly requested smoke checks or authorized all-tools acceptance against a configured JishuDB MCP connector and produces an evidence-based Markdown report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify an already configured JishuDB MCP connector, compare its available tools with the packaged contract, and document test results and cleanup. Read-only smoke checks are the default; all-tools acceptance requires scoped approval for temporary resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: All-tools acceptance creates temporary resources and may leave them behind if cleanup fails.

Mitigation: Require scoped approval, operate only on resources created in the current run, verify cleanup, and report remaining IDs if cleanup fails.

Risk: Synchronizing an existing source could affect user data.

Mitigation: Require separate explicit approval naming the existing source or knowledge base; never update or delete existing user resources.

Risk: Connector credentials or upload authorization could leak through test reports.

Mitigation: Redact credentials, authorization values, fixture Base64 data, local paths, and complete imported URLs from reports.

## Reference(s):

- [Contract baseline](references/contract-baseline.md)
- [Test cases](references/test-cases.md)
- [Fixture values](references/fixture-values.md)
- [Report template](references/report-template.md)
- [Project homepage (listed in release metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-mcp-check)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown acceptance report with test results, coverage gaps, and cleanup status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed outcomes without exposing credentials or fixture contents.]

## Skill Version(s):

0.1.4 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
