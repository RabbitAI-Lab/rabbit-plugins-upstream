## Description:

Analyzes authorized fixed-camera elder-care video to detect loneliness-related behavior signals, calculate a loneliness index, and return non-diagnostic warm-companionship recommendations and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External elder-care operators, family-care applications, and developers integrating smart-aging workflows can use this skill to analyze authorized home, private-room, or day-care video for behavior-based loneliness signals. The skill returns structured, non-diagnostic observations, companionship action suggestions, and historical report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive private-room elder-care video through cloud APIs.

Mitigation: Deploy only after explicit authorization from the elder, family, and operator; verify backend endpoints, retention policy, tenant/account binding, and report access controls before use.

Risk: Silent identity and token persistence can make reports or history appear under an unintended account or tenant.

Mitigation: Use a dedicated, reviewed runtime identity per deployment and confirm historical report access boundaries before enabling real footage analysis.

Risk: Arbitrary video URLs or shared/default identities could expose private footage or reports.

Mitigation: Restrict accepted URLs to trusted storage, avoid shared/default identities for production, and validate that report links are accessible only to authorized caregivers.

Risk: Behavioral loneliness scoring can be mistaken for a medical diagnosis or used without consent.

Mitigation: Present outputs as non-diagnostic behavioral observations and companionship suggestions, and require consent before monitoring or triggering smart-speaker or family-app actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-comfort-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON content and report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include loneliness index, behavior metrics, warm-companionship actions, family-facing summaries, historical report lists, and optional saved output files.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
