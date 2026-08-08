## Description:

投标机会顾问 helps bidding and sourcing teams assess public bid opportunities against a company profile, pricing history, competitor signals, and stated confidence before deciding whether to pursue a bid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chesaram](https://clawhub.ai/user/chesaram)

### License/Terms of Use:

MIT-0

## Use Case:

Bidding, sales, and sourcing teams use this skill to evaluate whether specific procurement notices or opportunity classes fit their company's qualifications, region, products, and capacity. It produces Go/No-Go guidance, confidence notes, competitor and pricing context, open-bid action lists, and optional self-contained HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store company profile and bidding context locally when the user creates ~/.bidprofile.json.

Mitigation: Create or update the profile only with explicit user intent, keep sensitive bid information out of shared workspaces, and review local files before reuse or distribution.

Risk: The skill may search or fetch public procurement pages and can optionally use a configured third-party data source credential.

Mitigation: Use public sources by default, provide credentials only when intentionally using a configured data source, and confirm that fetched records are appropriate for the bidding workflow.

Risk: Generated Go/No-Go advice and reports can influence commercial bid decisions.

Mitigation: Treat outputs as decision support, verify procurement records and assumptions, and have qualified reviewers approve final bid decisions and external reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-opportunity-advisor)
- [Data sources and collection strategy](artifact/references/data_sources.md)
- [Fit scoring and Go/No-Go decision framework](artifact/references/decision_framework.md)
- [Architecture notes](artifact/architecture.md)
- [Self-test coverage](artifact/SELFTEST.md)
- [China Government Procurement search](https://search.ccgp.gov.cn/bxsearch)
- [China Tendering and Bidding Public Service bulletin site](https://bulletin.cebpubservice.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional JSON records, shell commands, configuration snippets, and self-contained HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go/No-Go recommendations include reasoning and confidence; generated reports use local inline assets and should be reviewed before sharing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
