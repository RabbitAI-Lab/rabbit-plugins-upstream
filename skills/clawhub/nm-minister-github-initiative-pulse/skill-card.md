## Description:

Generates markdown digests and CSV exports for GitHub initiative health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and project leads use this skill to summarize GitHub initiative health, prepare stakeholder status updates, and create reusable markdown or CSV reporting outputs from tracker and GitHub board data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitHub, project, dashboard, or status triggers may activate the skill for general reporting requests.

Mitigation: Confirm that the requested task is a GitHub initiative-health reporting workflow before applying the generated templates or summaries.

Risk: Generated markdown comments could include stale or misleading status details if tracker or GitHub board data is outdated.

Mitigation: Refresh the tracker or GitHub Projects data and review generated comments before posting them to public issues, PRs, or Discussions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-minister-github-initiative-pulse)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown with tables, checklist snippets, status templates, and CSV-oriented reporting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-reviewed GitHub issue, PR, and Discussion content; no credential or external tool execution behavior was identified in the security evidence.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
