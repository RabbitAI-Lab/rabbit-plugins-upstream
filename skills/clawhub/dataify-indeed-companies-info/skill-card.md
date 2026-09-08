## Description:

Collect Indeed company records by company-list URL, keyword, industry and state, or company URL. Do not use for Indeed job listings or Glassdoor company URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify collection tasks for Indeed company information and receive the collected results. It supports collection by company list URL, keyword, industry and state, or company URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill submits external Dataify scraping tasks that may consume account credits.

Mitigation: Review task scope before large, multi-page, or multi-input runs and avoid resubmitting a paid task when a task ID can be resumed.

Risk: The skill needs a Dataify API token to submit tasks.

Mitigation: Set the token through a secure environment or secret manager, verify only that it is present, and do not paste or print the token in chat.

Risk: Security evidence marks the release suspicious because API-token guidance is inconsistent while the skill submits external paid scraping tasks.

Mitigation: Review credential handling and task-submission behavior before deployment, following the security guidance in the release evidence.

## Reference(s):

- [Dataify Indeed Companies Info API Reference](references/indeed_companies_info_api.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID, resume command, summarized result, or final JSON result depending on task completion and user-requested wait behavior.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
