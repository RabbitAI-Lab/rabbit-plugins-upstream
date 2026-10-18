## Description:

Screens newborn facial images or short videos for visible skin and scleral yellowing and provides a preliminary jaundice-risk indication and recommended next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and neonatal care teams can use this skill to review newborn facial images or short videos for preliminary jaundice-risk hints and guidance on seeking clinical follow-up. It also supports retrieving prior screening reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive newborn images and report metadata may be uploaded to the publisher's cloud service.

Mitigation: Obtain explicit guardian consent before use; review cloud endpoints and retention and deletion practices before sharing data.

Risk: The skill silently creates or reuses an identity and stores tokens locally, potentially linking reports to a persistent identity.

Mitigation: Confirm how accounts and tokens are created, stored, and removed, and require user confirmation before retrieving report history.

Risk: Visual jaundice screening may be inaccurate or mistaken for a clinical diagnosis.

Mitigation: Treat results only as preliminary hints; seek professional assessment and bilirubin testing rather than relying on the output for diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [Screening API and output fields](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary risk level, supporting observations, recommended action, and optional history links; not a diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled SKILL.md declares 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
