## Description:

Analyzes pet eye images or videos for visible redness, tearing, and cloudiness, and returns anomaly alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary teams use close-up pet images or videos to screen for visible eye abnormalities and review prior reports. Results are visual alerts, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos and report history are processed by the publisher's cloud service using a generated or reused identity and locally stored tokens, with limited privacy disclosure.

Mitigation: Obtain explicit consent before uploads or history queries; avoid sensitive home footage until retention, deletion, and account-scope controls are documented.

Risk: Visual alerts could be mistaken for a veterinary diagnosis.

Mitigation: Treat results as screening guidance and consult a veterinarian for suspected eye problems.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON or Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity alerts, report links, and a Markdown table of prior reports.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata; bundled skill frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
