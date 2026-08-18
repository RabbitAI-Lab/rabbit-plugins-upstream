## Description:

Skill Consolidator scans installed AI agent skills, rules, and commands to identify name collisions, functional overlap, trigger conflicts, and version differences, then produces cleanup reports and categorized indexes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alancouny](https://clawhub.ai/user/alancouny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to audit installed skills and rules before installing, merging, disabling, or reorganizing them. It helps identify duplicate names, overlapping behavior, trigger conflicts, and version drift across common AI agent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local AI-agent skill, rule, command, and instruction files while scanning for conflicts.

Mitigation: Install it only when local skill inventory scanning is acceptable, and use stdout-only reporting with --no-write when a persistent report is not needed.

Risk: Cleanup, merge, disable, or rewrite actions could change how installed agent skills are selected or triggered.

Mitigation: Review affected paths and proposed changes before approving any cleanup action; the documented workflow gates write actions on explicit user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alancouny/skills/skill-consolidator)
- [Server-resolved GitHub source](https://github.com/alancouny/skill-consolidator/tree/main/skill-consolidator)
- [Project homepage](https://github.com/alancouny/skill-consolidator)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports, JSON summaries, and concise guidance with shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default report output is a local Markdown file; stdout-only and JSON modes are available.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter and _meta.json report 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
