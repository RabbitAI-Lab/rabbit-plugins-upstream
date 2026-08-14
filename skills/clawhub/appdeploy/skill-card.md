## Description:

Deploy web apps with backend APIs, database, file storage, AI operations, authentication, realtime, and cron jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[avimak](https://clawhub.ai/user/avimak)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to publish, update, and manage AppDeploy-hosted websites and web apps with public URLs. It supports workflows for app templates, SDK feature references, deployment status checks, source inspection, secrets, versions, and custom domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The .appdeploy API key grants administrative access to deploy and manage apps.

Mitigation: Keep the key out of repositories and logs, restrict file permissions, and rotate it if exposed.

Risk: Administrative actions can delete apps, remove secrets, change domains, or read deployed source snapshots.

Mitigation: Require explicit confirmation before destructive or sensitive app-management actions.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API-key setup, deployment calls, status polling, source inspection, secret management, and domain configuration.]

## Skill Version(s):

1.0.8 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
