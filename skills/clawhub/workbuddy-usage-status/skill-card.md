## Description:

Generates an offline WorkBuddy usage dashboard from local WorkBuddy data, showing token use, credit estimates or opt-in precise credit, model distribution, thinking efficiency, errors, date filters, and usage spikes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users use this skill to inspect their own local usage, reconcile token and credit trends, and identify high-cost days, models, sessions, and errors. It is scoped to WorkBuddy local/account usage and is not a generic dashboard generator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated dashboard and data files can summarize local session titles, model usage, token counts, credit estimates, and error details.

Mitigation: Keep generated files in user-controlled locations and share them only with trusted recipients.

Risk: The optional --billing-token-file path uses a user-supplied WorkBuddy billing credential.

Mitigation: Use this option only for precise credit reconciliation, treat the token file like a password, avoid committing or sharing it, and delete or invalidate it after use.

Risk: Default credit values are local estimates and may not match precise server billing totals.

Mitigation: Use token totals as the primary usage metric, and use a WorkBuddy usage export or the explicit billing-token option when precise credit is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [README](README.md)
- [Data Guide](DATA-GUIDE.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [files, shell commands, guidance]

**Output Format:** [HTML dashboard, JSON data, JavaScript data wrapper, copied Chart.js asset, and concise completion guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default workflow is local and offline; optional xlsx or user-supplied billing token paths can refine credit calculations.]

## Skill Version(s):

1.3.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
