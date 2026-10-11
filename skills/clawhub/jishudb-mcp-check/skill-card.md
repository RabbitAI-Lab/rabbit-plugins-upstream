## Description:

Runs explicitly requested read-only checks or authorized all-tools acceptance of a configured JishuDB MCP connector and reports observed results and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to smoke-test an already configured JishuDB MCP connector or, with explicit approval, run isolated acceptance tests across its tools and review the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: All-tools acceptance creates temporary knowledge bases, documents, notes, jobs, and uploads in the selected JishuDB profile.

Mitigation: Default to read-only smoke checks; require explicit approval for all-tools mode, restrict changes to run-created resources, and report cleanup failures.

Risk: Connector testing may expose credentials or upload authorization values in tool responses.

Mitigation: Exclude credentials, authorization values, and fixture payloads from reports and other output.

## Reference(s):

- [JishuDB MCP Check project homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-mcp-check)
- [Contract baseline](references/contract-baseline.md)
- [Acceptance test cases](references/test-cases.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown acceptance report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed results, coverage gaps, cleanup status, and redacted evidence.]

## Skill Version(s):

0.1.4 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
