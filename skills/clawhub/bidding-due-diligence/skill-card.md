## Description:

Generates bidding-data due-diligence reports for one company or side-by-side company comparisons, covering operating activity, customers and suppliers, award trends, competitors, and public risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external business users, investors, procurement teams, and deal teams use this skill to assess a company's operating reality before investment, acquisition, partnership, supplier selection, or contract signing. It uses Zhiliaobiaoxun bidding data and public web risk searches to produce a report with cited records, data boundaries, and cautious wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives company queries submitted for due-diligence analysis.

Mitigation: Install only when this data sharing is acceptable for the user's organization; avoid submitting sensitive or confidential company names unless approved.

Risk: Automatic trial registration collects a persistent MAC-derived device hash and stores credentials locally.

Mitigation: Prefer a manually managed API key when possible, and use automatic registration only after explicit user consent.

Risk: Generated reports can preserve full signed sk URLs that may act as sensitive share links.

Mitigation: Treat generated reports and signed links as sensitive, and limit sharing to intended recipients.

Risk: Security evidence marks the release suspicious because it stores credentials, uses a persistent device identifier, and preserves login-bypass links.

Mitigation: Review the skill before deployment and confirm these behaviors fit the target environment's privacy and credential-handling policies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/bidding-due-diligence)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [workflow.md](artifact/references/workflow.md)
- [api-quick.md](artifact/references/api-quick.md)
- [report-template.md](artifact/references/report-template.md)
- [auto-register.md](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report in conversation plus optional self-contained HTML report file; may include JSON input for the bundled HTML renderer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic trial registration; reports include cited bidding records, data-boundary notes, and signed Zhiliaobiaoxun links when returned by the API.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
