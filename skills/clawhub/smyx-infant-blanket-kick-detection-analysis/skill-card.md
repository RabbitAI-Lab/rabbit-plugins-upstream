## Description:

Analyzes night-time crib video or images to estimate infant blanket coverage, detect kicking or blanket slip events, and return alerts with structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant crib monitoring media for blanket coverage status, kicking events, low-cover alerts, and cloud report history. It is intended as an auxiliary monitoring aid and not a replacement for adult supervision or medical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send infant crib videos or supplied video URLs to external services for cloud analysis.

Mitigation: Use only with appropriate guardian consent, review the service retention and privacy terms, and avoid submitting media that is not necessary for the analysis.

Risk: The security evidence reports automatic identity linking, local account token storage, and cloud history retrieval.

Mitigation: Install only if the publisher and service are trusted, protect local account data, and review report-history access before deployment.

Risk: The security evidence identifies under-scoped or default development/private-IP service configuration.

Mitigation: Review and replace packaged service configuration with approved production endpoints before operational use.

Risk: Blanket coverage alerts are auxiliary monitoring signals and may be incorrect or incomplete.

Mitigation: Use outputs as caregiver-facing prompts for review, not as medical advice or a substitute for adult supervision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant blanket kick detection API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis output, with optional report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write analysis output to a caller-provided file path.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
