## Description:

Workbuddy Usage Status generates an offline dashboard for a user's local WorkBuddy usage data, covering token consumption, credit estimates, model distribution, thinking efficiency, errors, and usage spikes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users and administrators use this skill to inspect their own local WorkBuddy usage, generate an auditable dashboard, and export supporting usage data for cost, model, and error review. It is scoped to WorkBuddy local/account usage and is not a generic analytics dashboard for other products or arbitrary datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML, JSON, JavaScript, CSV, and archive files can contain private WorkBuddy session titles, error snippets, and up to 300 characters of prompt text.

Mitigation: Treat generated files as private, review them before sharing or committing, and avoid publishing reports that contain sensitive local usage details.

Risk: The optional --billing-token-file mode uses a manually copied WorkBuddy session credential to request precise billing data from workbuddy.cn.

Mitigation: Use this mode only when precise billing data is needed, keep the token file local with restricted permissions, and delete the file or invalidate the session after use.

Risk: Credit values are local estimates unless an exported usage spreadsheet or the optional billing API mode is used.

Mitigation: Present token counts as the primary metric, label estimated credit clearly, and use the documented precise-credit options for reconciliation.

Risk: WorkBuddy trace history may be incomplete if local traces are cleaned before the skill archives them.

Mitigation: Run the skill at least every 30 days, or seed from an older snapshot when only historical daily totals are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [Publisher profile](https://clawhub.ai/user/clancy-feng)
- [README](artifact/README.md)
- [Data guide](artifact/DATA-GUIDE.md)
- [Changelog](artifact/CHANGELOG.md)
- [License](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [Files, HTML, JSON, CSV, JavaScript, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated local dashboard files: HTML, JSON, JavaScript, CSV, and a copied Chart.js asset.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default execution is local and offline. Optional precise billing mode can make a WorkBuddy API request only when the user supplies a token file.]

## Skill Version(s):

1.4.1 (source: frontmatter, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
