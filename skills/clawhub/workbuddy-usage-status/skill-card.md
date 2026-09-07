## Description:

Offline dashboard for WorkBuddy local usage analytics, with token consumption as the primary metric and credit as a local estimate, covering thinking efficiency, model distribution, cost-performance, date filtering, error monitoring, and usage-spike inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

External WorkBuddy users and developers use this skill to generate a local dashboard from their own WorkBuddy usage data for cost monitoring, model comparison, error review, and usage reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain local usage details such as session titles, model names, token counts, credit estimates, and error summaries.

Mitigation: Store generated dashboard, JSON, and JavaScript files in a private location and review them before sharing.

Risk: The optional --billing-token-file path uses a user-supplied WorkBuddy session credential to fetch precise billing data.

Mitigation: Use this option only intentionally, protect the token file like a password, restrict file permissions, and delete it or log out after use.

Risk: Credit values are local estimates unless an explicit xlsx export or billing-token flow is used.

Mitigation: Treat local credit as approximate and use the documented opt-in precise credit sources for reconciliation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [Publisher profile](https://clawhub.ai/user/clancy-feng)
- [README.md](README.md)
- [DATA-GUIDE.md](DATA-GUIDE.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Code, Guidance]

**Output Format:** [Self-contained HTML dashboard, JSON data, JavaScript data wrapper, and brief user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files are local snapshots; precise credit data requires opt-in xlsx import or a user-supplied billing token.]

## Skill Version(s):

1.3.2 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
