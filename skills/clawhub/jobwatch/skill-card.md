## Description: <br>
Jobwatch monitors user-selected company career pages, evaluates postings against the user's job-search profile, sends match alerts and digests, archives postings, tracks application status, and answers questions about watched jobs after explicit onboarding consent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ywc668](https://clawhub.ai/user/ywc668) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OpenClaw users use this skill to run a personal job-search watcher for companies they explicitly configure, including profile-based job matching, alerts, daily summaries, archival, application tracking, and follow-up queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process sensitive job-search profile data and send watched URLs, job descriptions, archived postings, questions, or notifications to optional external services. <br>
Mitigation: Use the default local or agent modes where appropriate, grant egress only to specific destinations through JOBWATCH_EGRESS_ALLOW or onboarding consent, and review the destination list before enabling optional services. <br>
Risk: Host credential reuse can increase blast radius if broadly enabled. <br>
Mitigation: Prefer dedicated per-skill API keys and, when host reuse is needed, grant only the specific JOBWATCH_ALLOW_HOST_CREDS scope required for that integration. <br>
Risk: Cron registration creates ongoing automated monitoring and notifications. <br>
Mitigation: Enable cron only after explicit consent and disable the jobwatch cron entries when the watcher should stop running. <br>
Risk: Application tracking records sensitive local status and notes about the user's job search. <br>
Mitigation: Keep the jobwatch data directory out of shared or synced folders and delete the local jobwatch state when the user wants to erase these records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ywc668/skills/jobwatch) <br>
- [Project homepage](https://github.com/ywc668/jobwatcher) <br>
- [Chinese skill reference](references/SKILL.zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with occasional shell commands and JSON configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include onboarding prompts, job-match judgments, alerts, digests, application-status updates, and job-search query answers.] <br>

## Skill Version(s): <br>
1.2.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
