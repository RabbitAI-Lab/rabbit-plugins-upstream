## Description:

Huawei Cloud ModelArts training job fault diagnosis skill that uses hcloud CLI to call ModelArts training job log and event APIs, analyze failed, timed-out, abnormal, or stuck jobs, and provide diagnosis conclusions with fix suggestions and confidence levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to diagnose Huawei Cloud ModelArts training job failures, timeouts, abnormal states, and stuck runs. It helps collect read-only job details, events, stages, and logs, then produces a concise diagnosis report with confidence-scored root causes and fix suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary flags risky setup and cleanup shell commands.

Mitigation: Install hcloud only from reviewed, verified, preferably pinned installers, and back up ~/.hcloud before running cleanup commands.

Risk: Account-wide discovery can be under-scoped.

Mitigation: Scope diagnosis to a specific training job, region, or time range when possible, and use least-privilege read-only credentials.

Risk: hcloud configuration, training logs, and OBS log URLs may expose sensitive information.

Mitigation: Do not paste AK/SK values, full hcloud config output, full logs, or OBS log URLs into shared chats; extract only minimal error or traceback lines.

## Reference(s):

- [API Catalog](references/api-catalog.md)
- [Diagnosis Flow](references/diagnosis-flow.md)
- [Command Templates](references/hcloud-command-templates.md)
- [Confidence Rules](references/confidence-rules.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown diagnosis report with inline hcloud commands and confidence labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include only key error or traceback lines and should not display full logs or credentials.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
