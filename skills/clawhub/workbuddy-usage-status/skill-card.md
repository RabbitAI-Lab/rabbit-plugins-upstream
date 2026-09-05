## Description:

Creates an offline WorkBuddy usage dashboard from local WorkBuddy data, showing token and credit usage, model distribution, thinking-efficiency metrics, errors, and usage spikes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users use this skill to inspect their own local WorkBuddy usage, cost, model, error, and efficiency patterns without sending default reports over the network. Developers or support teams can also use the generated local files for offline review and reconciliation, especially when comparing estimated credit with optional exported billing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain private local usage details such as session titles, model usage, and error snippets.

Mitigation: Keep generated HTML, JSON, and JavaScript reports local unless the user deliberately chooses to share them.

Risk: The optional --billing-token-file path uses a user-supplied browser session credential.

Mitigation: Use this mode only after explicit user opt-in, keep the token file local, avoid committing or sharing it, and revoke the session by logging out if it is exposed.

Risk: Credit values are locally estimated unless a precise xlsx export or functioning opt-in billing path is used.

Mitigation: Treat local credit as approximate and use exported WorkBuddy billing data when exact reconciliation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [README](artifact/README.md)
- [Data Guide](artifact/DATA-GUIDE.md)
- [Changelog](artifact/CHANGELOG.md)
- [WorkBuddy usage export page](https://www.workbuddy.cn/profile/plans-usage)

## Skill Output:

**Output Type(s):** [shell commands, files, json, html, guidance]

**Output Format:** [Local self-contained HTML dashboard plus JSON and JavaScript data files, with concise agent guidance for presenting the generated dashboard.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces timestamped reports and does not overwrite previous dashboard files.]

## Skill Version(s):

1.3.0 (source: frontmatter and changelog, released 2026-09-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
