## Description:

Using fixed cameras in kindergartens or early-education centers, the system analyzes multi-person video to detect social-interaction behaviors among children, including approach (distance < 1 m), conversation (face-to-face with mouth movement), and cooperative play (collaborative play, chasing, etc.).

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and early childhood center staff can use the skill to review interaction frequency, duration, and patterns in classroom or playground video as an educational reference. The results are visual behavior summaries and do not provide a psychological or developmental diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scanners report possible transfer of children's video to a service and automatic account creation.

Mitigation: Obtain guardian and organization consent, and confirm the service's data handling and retention before submitting videos; use approved test footage first.

Risk: Security scanners report local credential handling and warn that a no-analysis option may not prevent analysis from running.

Mitigation: Review identity and credential behavior before use, avoid exposing sensitive credentials, and do not rely on the no-analysis option when supplying private video.

Risk: The security review was partial because a referenced local path could not be resolved.

Mitigation: Review the affected reference and its related behavior before deploying the skill with real children's footage.

## Reference(s):

- [API interface and output fields](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Text]

**Output Format:** [Structured interaction analysis results and report links; Markdown for report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interaction counts and durations, initiator statistics, candidate low-interaction alerts, heatmap links, and a report export link.]

## Skill Version(s):

1.0.18 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
