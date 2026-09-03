## Description:

Computes DORA delivery-performance metrics from git and GitHub API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and release reviewers use this skill to compute DORA delivery-performance metrics from repository and GitHub data, classify performance tiers, and identify the weakest delivery dimension. It also supports audits of AI-assisted workflows by comparing change failure, lead time, restore time, and deployment frequency across cohorts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be misleading when the production branch, release cadence, failure labels, or GitHub issue metadata do not match the team's real deployment process.

Mitigation: Confirm the branch and labels before use, rerun over a narrower window, and sample contributing issues or pull requests to verify the underlying data.

Risk: The skill may activate on broad engineering-management terms and propose metrics work in an unrelated context.

Mitigation: Review the requested task and generated commands before running repository or GitHub analysis.

Risk: Optional plugin or charting-tool installation can add dependencies outside the core DORA metrics workflow.

Mitigation: Review optional installs separately and use them only when trend charting or the broader plugin experience is needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-minister-dora-metrics)
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister)
- [kuva Charting Reference](https://github.com/Psy-Fer/kuva)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and optional text or JSON metric reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include per-metric values, tier classifications, overall tier, and a bottleneck key.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
