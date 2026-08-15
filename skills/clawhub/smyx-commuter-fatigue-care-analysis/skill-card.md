## Description:

Analyzes fixed smart-home living-room video, with optional audio, to estimate after-work fatigue signals such as slumped posture, facial fatigue cues, frequent blinking, and sighing, then returns a structured fatigue report with care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home developers use this skill to analyze a home-arrival video window for fatigue-related posture, facial, and behavior signals, then receive a fatigue index, care-action recommendations, report links, and history lookups. It is positioned as wellness support and should not be used for medical diagnosis or employment, insurance, or other third-party monitoring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive in-home video or optional audio may be processed by cloud services.

Mitigation: Use only with explicit consent from household members, avoid analyzing shared spaces without notice, and confirm whether camera/audio analysis can be disabled for unsuitable contexts.

Risk: The skill can create or reuse persistent local and backend identity records for report history.

Mitigation: Define retention and deletion controls before deployment, review local workspace data and account records periodically, and avoid running it in shared workspaces without identity separation.

Risk: Fatigue inference could be mistaken for medical or employment-relevant assessment.

Mitigation: Keep outputs limited to wellness-oriented care suggestions and prohibit use for diagnosis, employer reporting, insurance decisions, or other third-party monitoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON-like analysis results, fatigue scores, care recommendations, history lists, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a user-specified file; history mode returns structured report records from the configured cloud API.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
