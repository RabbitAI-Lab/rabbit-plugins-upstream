## Description:

Automated job search and application system for Clawdbot that searches job platforms, analyzes matches, generates tailored cover letters, fills application forms, and tracks application status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veeky-kumar](https://clawhub.ai/user/veeky-kumar)

### License/Terms of Use:


## Use Case:

External users use this skill to search for matching jobs across supported platforms, prepare tailored application materials, and submit or stage applications with dry-run and confirmation controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server scanner flags this skill as suspicious because it is designed for automated job applications and includes under-scoped guidance for platform evasion and personal data handling.

Mitigation: Install only after reviewing the workflow, keep dry-run and per-application confirmation enabled, and verify each application before submission.

Risk: The skill handles sensitive profile, resume, credential, and work-authorization information.

Mitigation: Store profile and credential data only in explicitly approved locations, use secure storage for credentials, and limit file permissions for local profile and result files.

Risk: Automated application flows may conflict with job-platform rules or submit inaccurate screening responses.

Mitigation: Use official APIs when available, do not use captcha-solving services or residential proxies, respect platform limits, and manually confirm factual answers before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/veeky-kumar/skills/job-auto-apply)
- [Publisher profile](https://clawhub.ai/user/veeky-kumar)
- [LinkedIn Jobs API documentation](https://developer.linkedin.com/docs/v2/jobs)
- [Indeed API documentation](https://opensource.indeedeng.io/api-documentation/)
- [Glassdoor developer documentation](https://www.glassdoor.com/developer/index.htm)
- [Wellfound documentation](https://docs.wellfound.com/)
- [Job Platform Integration Reference](artifact/platform_integration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON configuration examples and Python or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce application-tracking JSON when the bundled workflow script is run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
