## Description:

Generates an offline WorkBuddy usage dashboard from local WorkBuddy records, including token use, estimated credit use, thinking efficiency, model distribution, date filtering, error monitoring, and usage-spike analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users and teams use this skill to audit local WorkBuddy activity, inspect token and credit trends, compare model cost-performance, and generate a portable local usage report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local WorkBuddy usage records and produces report files that may reveal private activity, costs, project names, session titles, or model usage.

Mitigation: Run it only on trusted local machines, keep generated HTML, JSON, and JavaScript reports private, and review contents before sharing.

Risk: Credit values are local estimates unless a WorkBuddy usage xlsx export is provided, so daily credit attribution can be approximate.

Mitigation: Treat token usage as the primary metric and use the optional --credit-xlsx flow when precise credit reconciliation is required.

Risk: Corrupt trace files or unparsable credit records can make a generated report incomplete.

Mitigation: Check the extractor warnings and dashboard warning banner before relying on the report for audit or billing decisions.

Risk: Natural-language activation could generate a local usage report when the user did not intend to inspect WorkBuddy usage.

Mitigation: Invoke it with explicit WorkBuddy usage or dashboard wording and confirm the output location before sharing report files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [README.md](README.md)
- [DATA-GUIDE.md](DATA-GUIDE.md)
- [CHANGELOG.md](CHANGELOG.md)
- [WorkBuddy usage export page](https://www.workbuddy.cn/profile/plans-usage)

## Skill Output:

**Output Type(s):** [Shell commands, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with Python command examples; generated local HTML, JSON, and JavaScript report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a self-contained offline HTML dashboard plus usage-status.json and usage-status.js; optional xlsx input can refine credit totals.]

## Skill Version(s):

1.2.0 (source: frontmatter and changelog, released 2026-08-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
