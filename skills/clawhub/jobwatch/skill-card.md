## Description: <br>
Jobwatch monitors user-configured company career pages, evaluates postings against the user's job-search profile, sends match alerts and digests, archives postings, tracks applications, and answers questions about watched jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ywc668](https://clawhub.ai/user/ywc668) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers using OpenClaw use this skill to automate monitoring of explicitly configured career pages, compare new roles with their profile and constraints, and receive alerts, daily digests, application tracking, and queryable archives. It is intended for a user's own job search after explicit onboarding consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores sensitive job-search data such as resume details, visa needs, seniority, red lines, application history, and private notes. <br>
Mitigation: Install only if comfortable with local storage of this data, keep the data directory out of shared or synced folders, and delete the jobwatch workspace data to erase it. <br>
Risk: Optional integrations can send watched URLs, job descriptions, profile text, notification content, archived jobs, or questions to configured third-party services. <br>
Mitigation: Prefer default local and agent modes, grant egress per destination instead of using all, use local or self-hosted endpoints when possible, and use dedicated revocable API keys. <br>
Risk: Host credential reuse and scheduled monitoring increase the operational footprint of the skill. <br>
Mitigation: Avoid host credential reuse unless needed, scope JOBWATCH_ALLOW_HOST_CREDS to specific credentials, and enable cron only after explicit consent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ywc668/skills/jobwatch) <br>
- [Project homepage](https://github.com/ywc668/jobwatcher) <br>
- [Chinese skill reference](references/SKILL.zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with optional shell commands and JSON configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces onboarding questions, job-match alerts, daily digests, application-status updates, query answers, local profile/state files, and optional cron configuration.] <br>

## Skill Version(s): <br>
1.2.3 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
