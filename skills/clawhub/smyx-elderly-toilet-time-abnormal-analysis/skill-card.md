## Description:

Analyzes privacy-preserving bathroom doorway or silhouette-only video to track elderly toilet occupancy duration and produce abnormal-stay alerts when the configured threshold is exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and senior-care or home-security operators use this skill to analyze privacy-preserving bathroom monitoring video, identify entry and exit events, measure continuous occupancy, and surface abnormal stays for human follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bathroom-adjacent media and identifiers may be sent to cloud services.

Mitigation: Use only with explicit consent from the monitored person or legal caregiver, confirm backend endpoints and retention policies before deployment, and prefer doorway views or blurred/silhouette-only footage.

Risk: The skill silently creates and reuses a persistent local identity.

Mitigation: Do not deploy in production until identity creation, token storage, and account-linking behavior are clearly governed and reviewable.

Risk: Development or test HTTP endpoints may be present in configuration evidence.

Mitigation: Confirm production endpoints and remove or govern dev HTTP endpoint use before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with alert status, occupancy timing, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud APIs for analysis results and historical reports; supports basic, standard, and json detail modes.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
