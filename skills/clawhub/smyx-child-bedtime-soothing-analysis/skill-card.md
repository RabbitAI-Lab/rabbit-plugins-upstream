## Description:

Analyzes child bedroom audio and video for bedtime distress and nightmare awakenings, then provides soothing actions, parent alerts, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Guardians and developers of child sleep-monitoring tools use this skill to identify nighttime distress, suggest or trigger staged soothing, notify parents when needed, and review incident reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child bedroom audio and video or media URLs may be sent to Life Emergence cloud services.

Mitigation: Obtain explicit guardian consent; document access, retention and deletion rules, and provide pause and disable controls.

Risk: The service may silently create or reuse identities, persist tokens locally, and retain cloud history reports.

Mitigation: Disclose identity and report handling; provide account revocation and restrict report and notification access to authorized guardians.

Risk: Automated soothing or event detection may miss urgent distress or prompt inappropriate responses.

Mitigation: Require guardian oversight, promptly alert guardians for out-of-bed or high-severity events, and avoid using outputs as medical diagnoses.

## Reference(s):

- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Text or JSON reports with event classifications, soothing actions, parent alerts, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels and optional file output or historical report listings.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata; bundled frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
