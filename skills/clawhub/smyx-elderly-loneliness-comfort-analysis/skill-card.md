## Description:

Analyzes fixed-camera elder-care video to detect loneliness-related behaviors such as prolonged solitude, static gazing, sighing, and talking to oneself, then returns structured behavior statistics, a loneliness index, companionship suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External elder-care operators, caregivers, and developers use this skill to analyze consented home or private-room video for loneliness-related behavior signals and generate structured summaries, alert levels, and warm companionship recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles private elder-care video and report history through cloud APIs.

Mitigation: Install only with explicit consent from the monitored elder and family, use trusted HTTPS services, and define retention, deletion, and access controls for videos, tokens, reports, and exports.

Risk: The artifact silently manages local identity values and API credentials.

Mitigation: Review identity and token handling before deployment, disable silent account creation or API-key-file reuse where inappropriate, and require clear authorization for report history and export access.

Risk: Companion actions could intrude on the elder or be mistaken for family contact.

Mitigation: Require opt-out support, avoid excessive reminders, and use only genuine pre-recorded family voice messages rather than AI-cloned or synthetic family voices.

Risk: Behavior-based loneliness analysis can be misread as a medical or psychiatric diagnosis.

Mitigation: Present outputs as behavioral observations and companionship guidance only, and route serious mental-health concerns to qualified local professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-comfort-analysis)
- [API interface reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON text with structured analysis results, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the generated report text to a caller-provided output file.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
