## Description:

Analyzes indoor fixed-camera pet video for signs of vomiting or regurgitation, including characteristic movements and visible vomitus, and records event details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and veterinary care teams can use the skill to review indoor camera footage, summarize possible vomiting or regurgitation events, and view event history. Its results are visual observations and do not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports external handling of video and credentials, account creation and storage of personal data, and analysis that may run during an export-only operation; scanner coverage is partial.

Mitigation: Review the security verdict before installation, avoid sending sensitive footage, use only trusted service endpoints, and limit credentials and personal information shared with the service.

Risk: Visual detections may mistake similar movements such as coughing or stretching for vomiting, and the output is not a medical diagnosis.

Mitigation: Treat results as behavior observations, use a fixed camera with a clear view, and consult a veterinarian when events recur or appear urgent.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured analysis results and report links; history listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports event timing, frequency, behavior, and visible vomitus characteristics. Results are observational, may include false detections, and are not a veterinary diagnosis.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
