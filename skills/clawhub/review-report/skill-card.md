## Description:

Generates Amazon review analysis and VOC reports from a user's ASIN, including pain points, purchase motivations, trends, competitor comparisons, listing suggestions, exports, and archived online report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to ask in natural language for review summaries, VOC reports, trend analysis, competitor comparisons, listing improvements, alerts, and exports for a specified Amazon ASIN. The skill is intended to reduce manual review analysis by coordinating ARI authorization, data checks, paid analysis confirmation, report generation, archiving, and follow-up monitoring guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits through report generation, review collection, leaderboard queries, advice generation, and other paid analysis flows.

Mitigation: Use the documented quote and confirmation flow, ask before every paid action when appropriate, and honor explicit user requests such as 'only quote, do not execute'.

Risk: Some account rules may allow small paid operations to auto-confirm and execute without a separate confirmation prompt.

Mitigation: Before use, check the account's auto-confirm policy and consider setting it to ask before every paid action for tighter cost control.

Risk: The skill requires ARI API-key access and stores authorization locally or reads it from ARI_API_KEY.

Mitigation: Authorize only through the documented browser or local configuration flow, do not paste API keys into chat, and use an ARI account suitable for the intended access.

Risk: The skill can archive reports, export data, and change monitoring or schedule settings for products in the connected ARI account.

Mitigation: Confirm management actions such as schedule changes, watch creation, pause, resume, and deletion before executing them, and review exports before sharing.

Risk: Interrupted paid analysis may already have charged credits and archived a report.

Mitigation: Check existing reports or operation status before retrying a paid command so the same report is not generated and charged twice.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/review-report)
- [funewa publisher profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [User guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Natural-language summaries and Markdown reports, with CLI commands, configuration steps, report links, and CSV/Markdown/HTML exports when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ASIN/site scope, sample size, report ID, credits used, account balance, online report URL, and package-limited export links.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, CHANGELOG, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
