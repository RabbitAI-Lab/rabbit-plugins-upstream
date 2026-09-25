## Description:

Analyzes night video from a fixed home camera to detect lights-off timing and early-morning movement, compare those signals with a 7-14 day personal baseline, and produce a sleep-rhythm anomaly reminder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, family caregivers, community care workers, and developers can use this skill to analyze night camera video for sleep-rhythm deviation indicators and review current or historical anomaly reports. The output is a visual-rhythm support signal, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly private home night video and sends analysis data to cloud services.

Mitigation: Use only with explicit consent from the monitored person or authorized guardian, and require clear retention, deletion, sharing, and access-control practices before real care use.

Risk: Evidence.security reports that internal identity tokens can be persisted and reused in a way that may mix reports across users in shared workspaces.

Mitigation: Install only in a trusted, single-user workspace unless identity handling is fixed, and isolate workspaces and credentials per monitored person.

Risk: Sleep-rhythm anomalies can be caused by normal short-term events and should not be treated as diagnoses.

Mitigation: Treat alerts as prompts for human follow-up and further professional evaluation where appropriate, not as medical determinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented text with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured rhythm metrics, anomaly type, alert level, caregiver-facing message, report links, and historical report tables.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
