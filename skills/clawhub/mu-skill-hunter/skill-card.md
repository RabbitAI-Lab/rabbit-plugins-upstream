## Description:

Skill严选猎手 helps agents discover external skills across GitHub, ClawHub, SkillHub, and Skills.sh, review candidates before installation, and produce periodic skill trend reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to find external skills, compare results from multiple skill sources, run pre-installation safety review, and generate recurring trend reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal use may contact external services while searching for skills.

Mitigation: Review the configured sources before use and limit searches to sources acceptable for the deployment environment.

Risk: The skill can run unpinned Node-based CLIs and auto-install external tools.

Mitigation: Disable automatic setup where possible, install required CLIs through a controlled package workflow, and review tool versions before execution.

Risk: The skill may read a GitHub token from the user's shell profile.

Mitigation: Use a low-scope token only when needed, keep it out of skill files, and rotate it if exposure is suspected.

Risk: Weekly Cron reporting can push results to external messaging destinations.

Mitigation: Enable the Cron report only after confirming the schedule, destination, and audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-skill-hunter)
- [Search guide](references/search-guide.md)
- [Security levels](references/security-levels.md)
- [Weekly report template](references/weekly-report-template.md)
- [GitHub repository search API](https://api.github.com/search/repositories)
- [ClawHub](https://clawhub.ai)
- [SkillHub](https://skillhub.cn)
- [Skills.sh](https://skills.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON scan summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include summaries, links, and popularity signals; trend reports are formatted for message delivery.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
