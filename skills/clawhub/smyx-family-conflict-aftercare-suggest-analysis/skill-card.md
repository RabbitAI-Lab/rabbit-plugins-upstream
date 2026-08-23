## Description:

Analyzes family public-area camera and microphone media to detect conflict signals, assess calm-window status, and produce aftercare or safety-path suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to process household public-area audio/video inputs for conflict-event detection, calm-window assessment, aftercare prompts, safety-path escalation guidance, and historical report retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive household camera and microphone media may be sent to remote services for processing.

Mitigation: Use only with explicit household consent, verified HTTPS production endpoints, and clear controls for disabling processing and limiting history access.

Risk: Identity-linked history reports and local token persistence can expose sensitive family-conflict records.

Mitigation: Restrict report access to the intended household owner, provide deletion and opt-out controls, and review local token storage before deployment.

Risk: Aftercare prompts during active or severe conflict could increase safety risk.

Mitigation: Require the calm-window gate before aftercare, and route suspected violence, minors present, weapons, or injury signals to safety resources instead of aftercare.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-aftercare-suggest-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query remote APIs for analysis results and identity-linked history reports.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
