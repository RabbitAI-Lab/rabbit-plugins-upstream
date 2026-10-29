## Description:

默认3个月窗口，star必须>1000；无满足条件仓库时依次扩大到6/12/24/36/48/60个月，最晚回溯到GPT-4发布时间（2023-03-14）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to find a recently created, highly starred public repository from a maintained list of major technology-company organizations. It produces a concise repository summary and explains the project, the problem it addresses, and its approach from available README and repository metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a GitHub credential from OpenClaw settings without clearly disclosing that access.

Mitigation: Remove the automatic OpenClaw settings-file credential fallback and provide a dedicated, minimally privileged GitHub token explicitly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zengzuo613/skills/github-big-teach-latest-repo-explorer)
- [Organization list](artifact/references/organizations.json)
- [Output template](artifact/references/output_template.md)
- [GitHub organization repositories API endpoint](https://api.github.com/orgs/{org}/repos?type=public&sort=created&direction=desc&per_page=100)

## Skill Output:

**Output Type(s):** [Markdown, Text, Analysis]

**Output Format:** [Markdown report with repository metadata, candidate counts, and a concise project summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the selected time window and repository-selection statistics; the organization search is limited to the maintained list.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
