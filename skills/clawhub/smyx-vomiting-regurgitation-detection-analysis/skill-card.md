## Description:

Analyzes indoor fixed-camera video to identify possible pet vomiting or regurgitation, describe visible vomitus, and record event times and frequency for observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and animal-care teams can review indoor-camera footage for possible vomiting or regurgitation events, visible vomitus, and event frequency. The results are visual observations for monitoring and do not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags undeclared account and credential handling and broad credentialed network requests.

Mitigation: Independently review the account and credential behavior and network destinations before use; do not provide credentials until that review is complete.

Risk: The security review flags privacy and control issues in the video-analysis workflow.

Mitigation: Clarify what video and report data are sent or retained, who can access them, and how to disable analysis; avoid sensitive footage until these controls are clear.

Risk: The security scan is partial because a local path-like reference could not be resolved, leaving part of the evidence incomplete.

Mitigation: Resolve and review the referenced path before treating the security review as complete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured observation report; JSON detail or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event times, frequency, visible vomitus characteristics, monitoring suggestions, and report links; not a medical diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
