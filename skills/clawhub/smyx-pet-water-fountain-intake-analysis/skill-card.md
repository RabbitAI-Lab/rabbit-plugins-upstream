## Description:

Analyzes pet water-fountain videos to estimate drinking frequency, duration, and intake, compare results with historical patterns, and flag notable changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use fountain-area videos or URLs to review pets' drinking patterns, receive changes-in-intake alerts, and view historical reports. Intake estimates and health alerts are informational, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local pet-fountain footage or supplied video URLs are sent to cloud services for analysis.

Mitigation: Share only footage you are comfortable sending to the provider; check its retention and deletion practices before using sensitive household video.

Risk: The skill automatically creates or reuses a cloud-linked identity and queries reports associated with it.

Mitigation: Review whether automatic identity linking and cloud report history are appropriate before installing or using the skill.

Risk: Service tokens are stored in the workspace data directory.

Mitigation: Restrict access to workspace data and avoid sharing directories containing stored tokens.

Risk: Video-derived intake estimates and health alerts can be mistaken for a veterinary diagnosis.

Mitigation: Treat estimates as indicators only and consult a veterinarian about concerning changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Pet fountain analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown list of historical reports, with optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include estimated intake, change alerts, recommendations, and report links.]

## Skill Version(s):

1.0.12 (source: ClawHub server release; bundled frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
