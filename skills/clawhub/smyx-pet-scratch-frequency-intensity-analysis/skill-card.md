## Description:

Analyzes cat scratch post videos to estimate scratching frequency, session duration, and intensity, returning structured observations about behavior, stress indicators, and claw condition without diagnosing disease or prescribing behavior changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers use the skill to review scratching activity around a cat scratch post and receive structured behavioral observations from a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or URLs may be sent to lifeemergence.com services, including when export-only mode is used.

Mitigation: Treat analysis as a cloud upload and avoid sensitive footage until export-only handling is fixed.

Risk: Account tokens persist locally, and credential destinations lack safeguards.

Mitigation: Protect workspace data and wait for destination restrictions before using credentials with sensitive material.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON observation reports and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intensity is an estimate from observed vibration; results do not diagnose disease or prescribe behavior changes.]

## Skill Version(s):

1.0.14 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
