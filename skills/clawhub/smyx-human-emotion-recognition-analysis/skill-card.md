## Description:

Recognizes and summarizes multidimensional emotion signals from frontal face images or videos, including intensity scores, abnormal-emotion flags, trend information, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit face images, videos, or media URLs for emotion-recognition analysis and to retrieve structured reports or cloud-stored report history. It is suited to human-computer interaction and mental-health monitoring workflows where emotion outputs are treated as supportive reference data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, or URLs are sent to a remote analysis service and may create identity-linked emotion reports.

Mitigation: Install and use only after confirming user consent, data-retention expectations, and that the remote service is approved for the intended data.

Risk: The skill creates or reuses local identity state, can retrieve cloud-stored history, and may store tokens in a workspace SQLite database.

Mitigation: Run in an approved workspace, review local identity and token storage, and clear stored state when reports should not remain linked to the environment.

Risk: Endpoint configuration may include development or private-IP defaults for sensitive face and emotion data.

Mitigation: Verify configuration before deployment and use production-safe HTTPS endpoints approved for the release environment.

Risk: Emotion-recognition output may be mistaken for professional psychological or medical diagnosis.

Mitigation: Present results as reference information only and route persistent or concerning emotional signals to qualified professional review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured emotion-recognition results, abnormal-emotion flags, recommendations, report links, and historical report tables.]

## Skill Version(s):

1.0.12 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
