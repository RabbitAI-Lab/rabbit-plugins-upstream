## Description:

Using fixed-camera home or care-room video, this skill analyzes daily activity for loneliness-related behaviors such as prolonged solitude, static gazing, sighing, and talking to oneself, then returns a structured loneliness-support report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family-care platforms, and elder-care service developers use this skill to analyze elder activity video, produce structured behavior statistics, estimate a loneliness index, and suggest warm companionship actions. It should be used only with appropriate consent and human oversight.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive in-home or care-room video and optional audio through configured cloud APIs.

Mitigation: Use only with explicit consent from the elder and authorized caregivers; verify configured API endpoints, access controls, raw media retention, and report retention before deployment.

Risk: The skill silently creates or reuses identity-linked accounts and may store local tokens or account identifiers for report history and export links.

Mitigation: Restrict access to the local workspace data directory, audit stored identifiers and tokens, rotate or remove credentials when no longer needed, and limit who can open history or export URLs.

Risk: Loneliness estimates and companionship suggestions can be mistaken for clinical mental-health findings or may trigger unwanted interventions.

Mitigation: Treat outputs as behavior statistics and support suggestions, not medical diagnosis; keep human review in the care workflow and honor opt-out or reminder-shutdown requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-comfort-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown and structured JSON-style analysis reports, with optional report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include loneliness metrics, behavior summaries, companionship recommendations, historical report lists, and cloud report links.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
