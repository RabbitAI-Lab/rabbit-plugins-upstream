## Description:

Analyzes fixed smart-home camera video from the first 30 minutes after an office worker arrives home to estimate fatigue indicators and suggest gentle smart-home care actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home agents use this skill to analyze home-arrival video or URL inputs, produce fatigue-level reports, and retrieve cloud history for after-work care. It provides fatigue-event assessment and supportive recommendations, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home video or optional audio may be processed by backend services.

Mitigation: Review service endpoints before installation and use the skill only with informed consent from affected household occupants.

Risk: The skill can silently create or reuse a local identity and store tokens or history data.

Mitigation: Verify local identity/token storage, access controls, and deletion procedures before deployment.

Risk: Cloud history reports may retain sensitive fatigue and household-context data.

Mitigation: Confirm retention, deletion, and report-sharing controls before enabling history queries.

Risk: Fatigue assessments could be mistaken for medical conclusions.

Mitigation: Present outputs as fatigue-event observations and care suggestions, and avoid medical diagnosis or employment/insurance use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON reports with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue index, detected signals, care recommendations, cloud report links, and history tables.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
