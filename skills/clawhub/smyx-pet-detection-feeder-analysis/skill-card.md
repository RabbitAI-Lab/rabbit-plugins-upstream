## Description:

Detects and recognizes cats and dogs in feeder or IPC camera images and videos, supports pet identity enrollment, and returns structured analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart feeder operators can analyze images or videos from feeder and IPC cameras to identify cats or dogs, enroll pet identities, and review detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security guidance reports account creation and credential handling beyond the stated pet recognition purpose.

Mitigation: Review the account and credential behavior before use, and run the skill only if that behavior is acceptable.

Risk: Video is processed externally, according to the security summary and guidance.

Mitigation: Confirm the service's data handling and submit only footage you are authorized and comfortable sending for external processing.

Risk: The analysis-only flag is reported as ignored, and the scan is incomplete because a referenced local path was missing.

Mitigation: Do not rely on that flag to limit behavior; review the relevant behavior and treat the security assessment as incomplete until the missing path is assessed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Links]

**Output Format:** [Structured analysis report in Markdown or JSON, with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file; supports basic, standard, and JSON detail levels.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
