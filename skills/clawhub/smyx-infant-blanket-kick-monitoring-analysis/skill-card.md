## Description:

Identifies babies kicking off blankets or exposing their bodies during sleep and alerts parents to cover them up to prevent catching a cold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant sleep images or videos for blanket-kicking, body exposure, and related reminder conditions. It can also query cloud-hosted historical monitoring reports tied to the resolved local identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant or nursery videos and URLs may be sent to the publisher's cloud service for analysis.

Mitigation: Use only with media that the user is comfortable sharing with the publisher, and confirm endpoint, retention, deletion, and access practices before deployment.

Risk: Reports are associated with an automatically created or reused local identity.

Mitigation: Tell operators that history queries are identity-linked and review account-linking behavior before using the skill with sensitive household data.

Risk: Service tokens may be stored in a workspace SQLite database.

Mitigation: Restrict workspace access, avoid committing generated data directories, and rotate or clear service credentials when decommissioning the skill.

Risk: Monitoring results are only an auxiliary reminder and may miss unsafe sleep conditions.

Mitigation: Keep human caregiving and infant safety practices as the primary safeguards; do not rely on this skill as a substitute for supervision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-monitoring-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown or JSON analysis report, with optional saved output file and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include monitoring results, recommendations, risk prompts, and report links returned by the publisher's cloud service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
