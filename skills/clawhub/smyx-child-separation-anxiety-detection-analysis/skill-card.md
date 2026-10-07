## Description:

Analyzes home or kindergarten drop-off videos for crying and resistance behaviors and reports a mild, moderate, or severe separation-anxiety level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and teachers can use drop-off footage to review a child's visible distress and receive behavioral summaries and supportive suggestions; this is not a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's and families' entrance videos or URLs are sent to a cloud analysis service.

Mitigation: Obtain appropriate consent and confirm the service's retention, access, and deletion practices before submitting minors' footage.

Risk: The skill silently creates or reuses an identity and stores tokens and profile data locally.

Mitigation: Review identity creation and local data protection before installation; restrict access to stored credentials and profile data.

Risk: Keyword-triggered history requests can retrieve prior cloud reports and report links.

Mitigation: Restrict report access to authorized users and confirm export-link handling and deletion options.

Risk: Visual behavior estimates may mistake play or incidental tears for anxiety and are not a diagnosis.

Mitigation: Review the footage and context with a caregiver; seek qualified professional assessment for persistent or severe concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or history list in text, Markdown, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior summaries, suggested actions, and links to current or prior cloud reports.]

## Skill Version(s):

1.0.12 (source: server release metadata; bundled SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
