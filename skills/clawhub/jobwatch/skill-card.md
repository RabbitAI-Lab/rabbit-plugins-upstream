## Description: <br>
Jobwatch turns an OpenClaw agent into a scheduled job-market watcher that monitors configured company career pages, evaluates postings against the user's profile with an LLM, sends alerts and digests, archives jobs, and tracks applications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ywc668](https://clawhub.ai/user/ywc668) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual job seekers and their agents use Jobwatch to monitor explicitly configured career pages, compare openings to the user's resume, seniority, visa, location, and role constraints, receive strong-match alerts and daily digests, archive postings, and track application status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Job URLs, job descriptions, notification text, and profile-derived criteria can be processed by configured third-party services. <br>
Mitigation: Review the Privacy & Data Flow section, keep the local knowledge-base and chat-channel defaults when possible, use self-hosted or dedicated service credentials, and enable optional integrations only when their data exposure is acceptable. <br>
Risk: The skill can register recurring job-monitoring tasks that continue scraping sources and sending notifications. <br>
Mitigation: Register cron only after explicit onboarding consent, review the configured sources and notification channel, and disable the jobwatch cron entries when monitoring is no longer needed. <br>
Risk: Host OpenClaw or Telegram credential reuse expands credential access beyond the skill's own configuration. <br>
Mitigation: Leave JOBWATCH_ALLOW_HOST_CREDS unset unless host credential reuse is necessary, and prefer dedicated API keys in the skill's own .env file. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/ywc668/skills/jobwatch) <br>
- [README](README.md) <br>
- [Chinese Skill Documentation](references/SKILL.zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text] <br>
**Output Format:** [Markdown instructions with shell commands, configuration updates, JSONL judgment records, and plain-text notifications.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local jobwatch profile, state, queue, run log, knowledge-base files, and optional cron entries after user consent.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
