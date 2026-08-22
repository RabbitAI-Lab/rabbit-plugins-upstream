## Description:

Analyzes acoustic features (frequency, duration, pitch, intensity) of livestock and poultry vocalizations to detect abnormal sounds such as coughing, wheezing, painful screams and hoarse calls, and outputs respiratory health risk hints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and farm operations teams use this skill to analyze livestock or poultry audio and video for acoustic signs of abnormal vocalizations, then review respiratory-health risk hints and historical report links. The output is intended for non-contact herd or flock screening, not veterinary diagnosis or treatment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media is processed by cloud backend services.

Mitigation: Use only recordings approved for cloud processing, avoid media containing unrelated sensitive audio, and review the configured service endpoints before deployment.

Risk: The skill can silently create or reuse a backend identity and store account tokens or profile data locally.

Mitigation: Run it in an isolated workspace, review identity and token handling before use, and clear or manage the workspace data database when persistent identity reuse is not desired.

Risk: Respiratory-health outputs are screening hints rather than clinical diagnoses.

Mitigation: Treat results as triage signals and confirm animal health decisions with a qualified veterinarian and appropriate lab testing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocalization-health-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Files]

**Output Format:** [Markdown text with structured JSON report content and report links; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local audio/video files or URLs, historical report listing, and basic, standard, or json detail modes.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
