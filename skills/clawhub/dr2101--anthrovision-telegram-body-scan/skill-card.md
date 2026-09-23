## Description:

Run end-to-end body-scan measurement flow in Telegram using AnthroVision bridge tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dr2101](https://clawhub.ai/user/dr2101)

### License/Terms of Use:


## Use Case:

External users use this skill to submit a Telegram body-scan video and required measurements, consent to processing, and receive grouped body measurements with a waist-to-hip summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Body-scan videos and related measurements are sensitive personal data.

Mitigation: Ask for explicit consent before processing a real person's video, prefer Telegram attachments, and avoid submitting videos of other people unless they have clearly consented.

Risk: External video URLs may expose users to unsafe or unintended network access patterns.

Mitigation: Accept only downloadable HTTPS video URLs and reject local paths, localhost, loopback, and private network URLs.

## Reference(s):

- [AnthroVision Telegram Body Scan on ClawHub](https://clawhub.ai/dr2101/skills/anthrovision-telegram-body-scan)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls]

**Output Format:** [Concise Markdown with deterministic status acknowledgements and grouped measurement results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses structured scan fields and avoids relaying arbitrary upstream tool strings.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
