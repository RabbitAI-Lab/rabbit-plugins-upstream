## Description:

Analyzes fixed-camera home or kindergarten drop-off video to identify crying facial expressions, clinging or resistance behaviors, and produce a mild, moderate, or severe separation-anxiety assessment with parent and teacher guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, and developers integrating school drop-off camera workflows use this skill to turn uploaded or URL-based child drop-off video into structured behavior observations, separation-anxiety level estimates, friendly reminders, and report links. The skill is assistive and explicitly does not replace evaluation by a child psychology professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles child, home, or kindergarten video through a configured cloud service.

Mitigation: Use only with explicit guardian consent, confirm retention and deletion expectations, and restrict use to authorized caregivers, teachers, or operators.

Risk: The security evidence states that account identity can be silently created or reused and auth tokens can be stored locally.

Mitigation: Review the installation environment before deployment, restrict workspace and database access, and clear local credentials when access should end.

Risk: Historical reports may contain sensitive child behavior data and can be queried by the skill.

Mitigation: Require explicit user intent before listing historical reports and verify that only authorized users can access report history.

Risk: Visual behavior analysis may confuse crying, play, environmental effects, or multiple children and is not a clinical diagnosis.

Mitigation: Treat results as assistive observations, review outputs before acting, and seek professional support for persistent or severe concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON report content, friendly guidance, historical report listings, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links; local video input is documented for mp4, avi, and mov files up to 10 MB.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
