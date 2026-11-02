## Description:

Helps candidates find and assess job openings, prepare applications, and track outcomes using verified resume information and browser automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaibhavarora14](https://clawhub.ai/user/vaibhavarora14)

### License/Terms of Use:

MIT-0

## Use Case:

External candidates use the agent to find suitable roles, assess fit, prepare and submit their own applications, and track confirmed outcomes. It is intended for explicit job-search and job-application requests, not general career advice or unrelated form automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submission helpers may weaken approval safeguards, including when a submission is resumed.

Mitigation: Keep personal oversight of every submission and require fixes to resumed-submission checks before relying on automation.

Risk: Profile-handling code may expose personal information.

Mitigation: Request fixes to macOS profile handling before relying on automation.

Risk: Telemetry and source sharing may share information if left enabled.

Mitigation: Disable telemetry and sources sharing separately before onboarding if you do not want sharing.

Risk: CAPTCHA assistance and public pull requests require separate safeguards.

Mitigation: Leave CAPTCHA assistance off and authorize public pull requests separately.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vaibhavarora14/skills/job-application-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Application guidance and tracking records]

**Output Format:** [Candidate-specific job-search guidance, application workflows, and tracking results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May handle sensitive resume and profile information and interact with browser-based application forms.]

## Skill Version(s):

3.8.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
