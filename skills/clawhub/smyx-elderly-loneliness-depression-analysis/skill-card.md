## Description:

Using fixed cameras at home (living room, bedroom) of elderly people living alone, the system analyzes daily videos and detects negative behavior indicators during solo time: dazing (long-duration motionless gazing without purposeful action), sighing (rapid chest rise-and-fall with audible expiration), and self-talking (mouth movement without any conversation partner).

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Family members and community care workers use this skill to review video-based behavior summaries and risk prompts for older adults living alone, supporting timely check-ins and care. It does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private footage may be uploaded even when the --export-env-only option suggests that analysis will not run.

Mitigation: Do not use private footage until the publisher fixes this behavior and clarifies upload recipients, retention, charges, and deletion controls. Obtain the recorded person's informed consent.

Risk: Automatic remote enrollment and local credential storage have unclear user controls.

Mitigation: Clarify enrollment and account handling before use, and protect the local credential database. Disable HTTP wire logging.

Risk: The --api-url option may not redirect processing as expected, and suggested face masking may not happen automatically.

Mitigation: Do not rely on that option to control where footage is processed or assume masking is applied; verify handling before sending sensitive footage.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured behavior summaries and risk prompts in JSON or text; history results can be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize observed behavior and suggested follow-up; they are not a depression diagnosis. Analysis accuracy and server-side safeguards are unverified.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
