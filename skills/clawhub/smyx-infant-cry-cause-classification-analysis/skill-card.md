## Description:

Analyzes infant cry recordings or videos to suggest possible causes, confidence levels, and caregiving guidance, with access to cloud-stored reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers use this skill to obtain possible explanations for infant crying from recordings and review prior analysis reports. Results are caregiving aids, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant recordings and report history are sent to a third-party cloud service, with unclear retention and deletion terms.

Mitigation: Obtain guardian consent before use and confirm the service's privacy, retention, and deletion terms.

Risk: The skill silently creates or reuses an identity and stores tokens in the local workspace data directory.

Mitigation: Review local token storage and access controls before installation; use only in an appropriate trusted workspace.

Risk: A predicted cause could be mistaken for a medical diagnosis.

Mitigation: Treat results as caregiving guidance only and seek pediatric care for persistent or unusual crying.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or Markdown report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested causes, confidence, caregiving hints, and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
