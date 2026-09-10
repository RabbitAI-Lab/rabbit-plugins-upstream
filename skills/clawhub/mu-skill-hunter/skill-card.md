## Description:

Discovers external AI agent skills across GitHub, ClawHub, SkillHub, and Skills.sh, supports pre-install security review, and can generate recurring trend reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to find external skills, compare sources, review candidate skills before installation, and receive curated skill trend reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill searches external services and may send search terms to third-party platforms.

Mitigation: Review search queries before execution and avoid including confidential project, credential, customer, or personal data.

Risk: The skill may guide installation of global third-party CLIs or a remote installer.

Mitigation: Review every install command, avoid curl-to-bash unless independently verified, and prefer pinned or manually inspected installation steps.

Risk: The skill can set up recurring reports and personalized profile data.

Mitigation: Enable Cron delivery and profile personalization only after explicit user consent, and document how to disable the schedule.

Risk: The security evidence notes that the skill overstates its privacy and safety posture.

Mitigation: Treat scanner output as advisory, keep human approval in the loop for installation decisions, and do not bypass review for medium, high, or extreme risk results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-skill-hunter)
- [Search strategy guide](references/search-guide.md)
- [Security levels](references/security-levels.md)
- [Weekly report template](references/weekly-report-template.md)
- [Landing page](https://muippt.github.io/mu-skill-hunter/)
- [GitHub REST API documentation](https://docs.github.com/en/rest)
- [ClawHub](https://clawhub.ai)
- [SkillHub](https://skillhub.cn)
- [Skills.sh](https://skills.sh)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, JSON reports, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include external skill search results, security-review summaries, install guidance, and scheduled report content.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter and changelog state 2.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
