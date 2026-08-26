## Description:

Analyzes fixed-camera aquarium videos to flag side-swim, upside-down, axial rotation, floating, or sinking posture anomalies and produce structured reports with abnormal-duration ratios and suggested user actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquaculture staff, and developers use this skill to analyze fixed-camera aquarium media, quantify abnormal swimming posture duration, review historical reports, and decide when to inspect water conditions or seek professional help.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media may be sent to a backend service and associated with an automatically selected identity.

Mitigation: Use only with authorized media, review endpoint configuration before deployment, and disclose or obtain consent where aquarium monitoring affects other parties.

Risk: Account tokens may be stored in a local workspace database with limited user control.

Mitigation: Inspect local storage behavior, restrict workspace access, and rotate or remove stored tokens when the skill is no longer needed.

Risk: Default private development endpoint configuration may be unsuitable for normal use.

Mitigation: Replace or document non-production endpoints before commercial deployment.

Risk: Visual posture analysis can be mistaken for veterinary diagnosis.

Mitigation: Treat outputs as posture and duration analysis only; use persistent or severe findings to prompt water-quality checks and qualified aquarium or veterinary consultation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [Fish abnormal swimming API documentation](artifact/references/api_doc.md)
- [Shared health analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON analysis reports with report links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload aquarium media to a backend API, poll for results, and query cloud report history.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
