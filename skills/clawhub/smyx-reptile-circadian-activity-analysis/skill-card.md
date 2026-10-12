## Description:

Analyzes fixed-camera reptile enclosure video to summarize hourly activity and compare day–night patterns with the species' natural rhythm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers, breeders, and developers use fixed-camera enclosure recordings to review hourly activity, identify possible day–night rhythm changes, and consult past reports. Findings support observation rather than veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure media and report history are sent to external cloud services.

Mitigation: Review the service destination and obtain consent before submitting media or accessing report history.

Risk: The skill creates or reuses a persistent local identity and stores service tokens in the workspace data directory with limited upfront disclosure.

Mitigation: Review this behavior before installing, restrict access to the data directory, and remove stored credentials when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis)
- [Reptile circadian analysis API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON or Markdown report and Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hourly activity, peak periods, rhythm assessments, alerts, and report links.]

## Skill Version(s):

1.0.15 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
