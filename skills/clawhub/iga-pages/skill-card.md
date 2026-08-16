## Description:

Deploy frontend and full-stack projects to IGA Pages, including project publishing, preview deployments, API routes, environment variables, and supported integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seasonrui](https://clawhub.ai/user/seasonrui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to deploy frontend and full-stack applications to IGA Pages, manage IGA Pages project configuration, and apply guidance for Pages Functions, environment variables, and Supabase integration binding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through cloud authentication and deployment actions.

Mitigation: Use it only when IGA Pages deployment is intentional, confirm authentication state before login, and review proposed deploy commands before execution.

Risk: Access keys, local environment files, and pulled project variables can expose secrets.

Mitigation: Prefer existing authenticated sessions or safer credential handling, avoid placing long-lived keys directly in shell commands where possible, and run env pull only on trusted machines with protected, gitignored .env.local files.

Risk: Preview URLs containing iga_token and iga_time can grant access to private deployments.

Mitigation: Treat tokenized preview URLs as private and share them only with intended recipients.

## Reference(s):

- [Environment Variables](references/env.md)
- [Serverless Functions](references/functions.md)
- [Integrations](references/integration.md)
- [Volcengine IAM key management](https://console.volcengine.com/iam/keymanage)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment URLs, environment-variable guidance, and project configuration steps.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
