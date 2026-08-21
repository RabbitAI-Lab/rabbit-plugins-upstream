## Description:

Triggers when a user provides a dog toilet or pet defecation-zone video URL or file, analyzes whether a pet defecation event occurred, and outputs a cleaning trigger signal after the pet leaves the area.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze fixed-camera pet toilet or defecation-area videos, identify the pet-entered, defecated, and pet-left event sequence, and produce a cleanup trigger that can be connected to a separate robot-vacuum or smart-home integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area videos or URLs are sent to the configured SMYX/LifeEmergence service for analysis.

Mitigation: Use only with appropriate consent and confirm the endpoint configuration before running analysis.

Risk: The skill can automatically create or reuse a local identity and store service tokens in workspace data.

Mitigation: Run it in a trusted workspace and review stored credentials on shared machines.

Risk: History lookup can query prior cloud reports associated with the resolved identity.

Mitigation: Use history commands only for authorized users and expected report scopes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Poop Auto-Clean API Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown reports or JSON analysis results, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return report links and history tables; supports local video files or video URLs for analysis.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
