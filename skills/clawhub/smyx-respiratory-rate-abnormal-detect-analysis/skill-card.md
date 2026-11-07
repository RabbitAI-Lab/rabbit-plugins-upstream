## Description:

Analyzes a resting pet video to estimate respiratory rate, compare it with species and body-size ranges, and flag readings that may need veterinary attention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and animal-care staff can submit a resting cat or dog video to estimate breathing rate, review an out-of-range alert, or retrieve prior monitoring reports. Results are for health monitoring and do not provide a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags credential and account side effects, including automatic account registration, and behavior beyond the stated pet-monitoring purpose.

Mitigation: Review identity initialization and remote-service behavior before use; run with a dedicated workspace identity and do not expose internal identity values.

Risk: Pet footage may be processed by a remote service.

Mitigation: Use only footage you are authorized to share and review the service's data handling before uploading private or identifiable video.

Risk: ClawScan cites unexpected file changes, and its analysis is partial because a reference is missing; the suspicious verdict does not establish malicious intent.

Mitigation: Clarify the flagged behavior and missing reference before installation; if proceeding, use an isolated workspace and inspect local changes after execution.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-respiratory-rate-abnormal-detect-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis report as text or JSON; history results can be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory monitoring only; it does not provide veterinary diagnosis or treatment advice.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
