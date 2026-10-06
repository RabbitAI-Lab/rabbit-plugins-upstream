## Description:

Analyzes children's behavior videos for repetitive movements such as spinning, hand flapping, and body rocking, and summarizes observed events and trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Therapists, caregivers, and special-education staff use this skill to summarize the frequency and duration of observed repetitive behaviors in children's videos and review prior reports. Its observations are not an autism diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's behavior videos, video URLs, and report queries are sent to external cloud services.

Mitigation: Obtain guardian consent before use, avoid identifiable footage where possible, and review the service's data-handling terms.

Risk: The skill may create a persistent local identity and store authentication tokens and profile data in the workspace.

Mitigation: Limit access to the workspace data directory, review what is retained, and remove stored identity data when no longer needed.

Risk: Ordinary movements or scenes with multiple people can produce misleading behavior classifications.

Mitigation: Have a qualified professional review sampled detections and do not use the reports as a diagnosis or prescription.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis)
- [Skill API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Text or Markdown behavior reports and report lists; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event counts, durations, trend summaries, and links to reports may be included.]

## Skill Version(s):

1.0.12 (source: server-resolved release; bundled frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
