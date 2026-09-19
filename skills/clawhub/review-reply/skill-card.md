## Description:

Generates buyer reply, platform appeal, and product-improvement guidance for Amazon negative reviews, with ARI-backed review analysis, alerts, monitoring, exports, and benchmarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to triage negative reviews, draft buyer replies and appeal guidance, analyze review trends, monitor product issues, and export reports or review data for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI actions can spend credits automatically under the service's auto-confirm rules or after the user changes confirmation settings.

Mitigation: Review quote and auto-confirm settings before paid actions; use 'only quote, do not execute' or ask-before-every-credit-deduction instructions when charges must be gated.

Risk: Schedule, watch, competitor, workbench, and auto-confirm actions can persist changes to the user's ARI account or future monitoring behavior.

Mitigation: Confirm account-affecting changes explicitly and review current schedule, watch, competitor, status, and auto-confirm settings before persisting them.

Risk: Interrupted paid analysis or collection may already have consumed credits and saved a report.

Mitigation: Check the latest report or operation status before retrying a confirmed paid command to avoid duplicate charges.

## Reference(s):

- [ARI CLI 与 API 参考](references/reference.md)
- [使用说明](使用说明.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-reply)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Natural-language responses, Markdown reports, JSON command results, CSV exports, and Markdown or HTML report exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI service-side data, pricing, confirmation, and account rules.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
