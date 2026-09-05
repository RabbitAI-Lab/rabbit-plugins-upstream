## Description:

Compares a primary Amazon ASIN with authorized competitors using product fields and review evidence to produce a static feature matrix that flags data gaps and experience differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill through an agent to compare a main ASIN against authorized competitors, using ARI product and review evidence to produce a feature matrix, identify data gaps, and highlight customer-experience differences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an ARI account for paid analysis and other actions broader than a static competitor feature matrix.

Mitigation: Install only when that ARI account access is intended, review quoted costs before paid operations, and keep auto-confirm disabled or tightly limited if every charge should require explicit approval.

Risk: Recurring monitoring, exports, and workbench status changes can affect account state beyond one-time report generation.

Mitigation: Treat schedule, watch, export, and workbench update commands as account-affecting actions and execute them only after the user asks for that specific action.

Risk: API-key use could expose the user's ARI account if credentials or request destinations are mishandled.

Mitigation: Use the local setup/configuration flow or ARI_API_KEY only, do not include keys in reports, and keep API requests on the official ARI endpoint unless the user explicitly enables a custom base URL.

Risk: The feature matrix is based on available product fields and review evidence, not sales, inventory, ads, orders, profit, or true return-rate data.

Mitigation: Label conclusions as evidence-based comparisons, preserve data gaps, and avoid unsupported operational or market-share inferences.

Risk: Retrying interrupted paid analysis can duplicate charges if the server already completed and archived the report.

Mitigation: Check report or operation status with the original ASIN or requestId before rerunning any confirmed paid command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-features)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown feature matrix and report prose with JSON CLI responses and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations, monitoring changes, exports, and account updates must follow the skill's quote and confirmation flow.]

## Skill Version(s):

1.4.5 (source: server release metadata, skill frontmatter, _meta.json, and ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
