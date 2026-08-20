## Description:

This skill helps an agent use Qinghu data interfaces to analyze Ozon Russia category hierarchy, growth, market size, and concentration signals to identify promising blue-ocean categories for new stores or product-line planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents supporting Ozon category research use this skill to compare Ozon Russia market trend, category detail, hot-category, and brand-ranking data before recommending two or three category opportunities and saturated categories to avoid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token and may expose that token through environment variables or request headers.

Mitigation: Install only where Qinghu API access is intended, scope token handling to the agent environment, and avoid sharing logs or transcripts that include authorization headers.

Risk: Large Ozon category datasets may be written to local spreadsheet or export files.

Mitigation: Review generated files before sharing them and handle exports according to the user's data-retention and access-control expectations.

Risk: Some Qinghu tools may consume paid Qinghu credits.

Mitigation: Require the agent to review the tool free/paid status and obtain authorization before calling paid tools, following the skill's stated authorization flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-bluesea-hunter)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, text, files]

**Output Format:** [Markdown guidance with optional JSON-RPC examples, shell commands, concise tables, and spreadsheet exports for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export local spreadsheet files when result arrays contain 10 or more records; recommendations should include data scope such as site, period, cycle, and sample size.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
