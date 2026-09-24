## Description:

Analyzes child surveillance images or videos to identify negative emotions, return structured reports and report links, and support cloud-based historical report lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, daycare staff, and operators use this skill to submit authorized child surveillance images or videos for emotion analysis and to retrieve cloud-hosted historical reports. Results are intended to support care decisions and do not replace adult supervision or emergency response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child surveillance media and analysis results are processed through LifeEmergence cloud services.

Mitigation: Use only with authorization and consent for the child media involved, avoid unnecessary uploads, and confirm retention and deletion practices before use.

Risk: Local identity and token state may be reused from workspace data files or a local database.

Mitigation: Run the skill in a dedicated, non-shared workspace and remove stored identity or token data when access should no longer persist.

Risk: Historical report queries may expose prior cloud-hosted reports for the current identity context.

Mitigation: Confirm account separation before querying history and restrict use to authorized caregivers or operators.

Risk: Emotion analysis can be incomplete or misleading and is not a substitute for in-person care.

Mitigation: Treat reports as decision support, review results before acting on them, and respond directly in urgent or safety-critical situations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown and JSON-formatted structured analysis text, with optional saved output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local media paths or public media URLs, supports historical report listing, and documents a 10 MB media-size limit.]

## Skill Version(s):

1.0.27 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
