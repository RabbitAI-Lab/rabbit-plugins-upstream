## Description:

Use when users need to bind an AIDSO API key in chat, price or submit a paid one-off GEO brand diagnosis, query task IDs without polling, retrieve raw AI conversations, or generate a Chinese HTML GEO diagnostic report with optional product-layer analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangyuanmile-coder](https://clawhub.ai/user/tangyuanmile-coder)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run paid AIDSO GEO brand-diagnosis jobs, manage explicit submission confirmation, query task results, and produce Chinese HTML diagnostic reports with optional product-level analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can submit paid AIDSO API jobs after user confirmation.

Mitigation: Review the quoted scope, platform choices, task count, and points before replying with the required confirmation text.

Risk: Task records, raw AI results, and normalized data are stored in the current workspace.

Mitigation: Use a dedicated workspace for sensitive client work and avoid sharing internal task folders as deliverables.

Risk: API keys are sensitive session credentials.

Mitigation: Bind keys only for the active session and avoid placing them in commands, files, logs, reports, or URLs.

## Reference(s):

- [AIDSO GEO API Reference](references/aidso-api.md)
- [GEO HTML Diagnostic Report Specification](references/report-spec.md)
- [HTML Report Model](references/report-model.md)
- [Report Model Example](references/report-model.example.json)
- [AIDSO API Key Management](https://geo.aidso.com/setting?type=apiKeyManage)
- [AIDSO GEO Question Pricing](https://geo.aidso.com/question)
- [AIDSO OpenAPI Base](https://openapi.aidso.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese user-facing text, Markdown command snippets, JSON working files, and UTF-8 HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses paid AIDSO API calls only after explicit confirmation and stores task records plus raw and normalized results in the current workspace.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
