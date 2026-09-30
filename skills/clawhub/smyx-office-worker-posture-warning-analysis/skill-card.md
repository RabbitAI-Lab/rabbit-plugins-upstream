## Description:

Analyzes office workstation video or image input to report prolonged sitting and posture warnings such as forward head posture, hunching, shoulder asymmetry, and close screen distance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace health, facilities, or enterprise wellness teams can use this skill to analyze office-camera footage or submitted workstation media for posture and prolonged-sitting alerts. The output is behavioral guidance and structured reporting, not medical diagnosis or rehabilitation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Office-camera footage and posture reports may contain sensitive employee personal data and are uploaded to cloud services.

Mitigation: Use only with employee notice and consent, approved cloud upload, and clear retention controls for reports and videos.

Risk: The skill silently creates or reuses persistent local identity and token records for analysis and report history.

Mitigation: Review identity and token storage before deployment and require explicit confirmation before analysis or history retrieval.

Risk: Posture warnings could be mistaken for medical diagnosis or treatment guidance.

Mitigation: Present outputs as workplace behavior prompts only and direct users with health concerns to qualified medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)
- [API interface reference](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured posture analysis report with warnings, metrics, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history and return report-list tables or export links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
