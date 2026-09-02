## Description:

Generates an offline local dashboard for WorkBuddy usage analytics, including token usage, credit estimates, thinking efficiency, model distribution, date filtering, error monitoring, and usage-spike inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

Developers and WorkBuddy users use this skill to inspect their own local WorkBuddy usage, cost, model behavior, errors, and activity trends in a generated offline dashboard. It is scoped to WorkBuddy local data and is not a generic analytics or dashboard-generation skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports can reveal session titles, work patterns, model usage, errors, timing, and credit estimates.

Mitigation: Keep the generated HTML, JSON, and JavaScript files in a private folder and share them only after reviewing their contents.

Risk: The --home and --credit-xlsx options can read an alternate WorkBuddy data root or billing export.

Mitigation: Use these options only with intentional, user-approved paths and billing exports.

Risk: Credit values are local estimates unless an exported usage spreadsheet is supplied.

Mitigation: Present local credit as an estimate and use --credit-xlsx when precise billing reconciliation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [README](artifact/README.md)
- [Data Guide](artifact/DATA-GUIDE.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Self-contained HTML dashboard plus JSON and JavaScript data files, with concise Markdown handoff text from the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated locally; the dashboard embeds its data and chart runtime for offline viewing.]

## Skill Version(s):

1.2.6 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
