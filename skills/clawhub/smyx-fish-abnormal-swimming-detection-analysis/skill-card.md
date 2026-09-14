## Description:

Analyzes aquarium camera images or videos to identify abnormal fish swimming postures such as side-swimming, upside-down posture, axial rotation, floating, or sinking, and returns structured monitoring results with suggested follow-up actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquarium operators, and developers use this skill to analyze fixed-camera aquarium media, quantify abnormal swimming duration, review historical monitoring reports, and decide when to inspect water quality or seek specialist help. The skill is a visual posture analysis aid and should not be treated as a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, media URLs, report history, identity state, and tokens may be sent to or stored by the publisher's backend.

Mitigation: Install only when the publisher and backend are trusted, and treat submitted media and report history as sensitive user data.

Risk: Packaged defaults can use plaintext HTTP development endpoints for service traffic.

Mitigation: Review configuration before deployment and replace default endpoints with HTTPS production endpoints.

Risk: The skill can create or reuse a persistent local identity without asking the user.

Mitigation: Review local identity/session handling and disclose persistence expectations before operational use.

Risk: Visual posture findings could be mistaken for a disease diagnosis or used to trigger aquarium controls without user approval.

Mitigation: Present results as visual monitoring signals only, require user confirmation before equipment changes, and direct urgent cases to qualified aquarium or veterinary specialists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface document](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include abnormal posture classifications, duration ratios, alert levels, suggested actions, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
