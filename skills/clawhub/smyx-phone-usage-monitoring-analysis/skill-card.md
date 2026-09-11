## Description:

Based on computer vision, this skill detects workplace phone usage in images or video streams, counts usage duration and frequency, and returns structured monitoring reports with warnings and suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise operators and workplace administrators use this skill to analyze office surveillance images or videos for phone-use behavior and produce structured reports for internal management review. The results should be treated as advisory and reviewed with privacy, labor, and consent requirements in mind.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes employee surveillance images or videos and may affect workplace privacy and labor compliance.

Mitigation: Use only after confirming workplace notice, consent, legal basis, retention limits, and human review procedures for any management decisions.

Risk: The security evidence reports silent identity linking, surveillance media upload, token storage, and insecure development HTTP endpoints.

Mitigation: Review before installation and avoid real employee media, identities, or credentials until production HTTPS endpoints, cloud recipient documentation, retention controls, and explicit scoped authentication are in place.

Risk: Computer-vision monitoring results can be inaccurate or misleading if used as the sole basis for discipline or performance assessment.

Mitigation: Treat results as advisory, review source media and context, and keep a human decision-maker responsible for any follow-up action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON monitoring report with analysis results, warnings, suggestions, and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include compliance scores, detected phone-use counts, duration summaries, area assessments, efficiency warnings, improvement suggestions, and links to generated reports.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
