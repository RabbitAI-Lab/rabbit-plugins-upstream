## Description:

Monitors WeChat public-account articles with the Mangyun API, builds a local incremental intelligence repository, and generates Chinese analysis briefs, dashboards, and Excel exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor public WeChat accounts, collect new articles through the Mangyun API, analyze new content in Chinese, and export intelligence dashboards and workbooks for competitive or industry tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Mangyun API calls can incur unexpected costs if scans or content fetches exceed the intended scope.

Mitigation: Run the built-in estimate and status steps, keep workspace budget controls enabled, and require explicit approval before using over-budget fetches.

Risk: The Mangyun API key could be exposed if copied into files, logs, prompts, screenshots, or exports.

Mitigation: Keep MANGYUN_API_KEY only in the environment and avoid writing credentials or full request headers to the workspace or generated outputs.

Risk: Generated JSON, dashboards, and Excel files can contain customer data such as article text, analysis, request IDs, balances, and errors.

Mitigation: Treat the workspace and generated files as customer data and share or retain them only under the user's data-handling requirements.

Risk: Article analyses may include unverified claims or ambiguous source statements.

Mitigation: Preserve original article links in exports and require users to verify important facts against the source articles.

## Reference(s):

- [分析结果导入规范](references/analysis-schema.md)
- [曼格云 API 调用规范](references/api-contract.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown guidance with shell commands, structured JSON analysis items, and generated dashboard and Excel file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local workspace state, budget controls, and environment-provided Mangyun API credentials.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
