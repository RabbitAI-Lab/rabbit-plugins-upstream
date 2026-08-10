## Description:

Using a night-time camera above a crib, this skill analyzes infant blanket coverage, identifies kicking or blanket-slip events, and outputs alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze crib camera images, videos, or URLs for visual signs that an infant's blanket coverage is low or has slipped after kicking. The output is an auxiliary monitoring report and alert, not medical advice or a replacement for adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant crib videos, images, URLs, and report history may be sent to the publisher's cloud service.

Mitigation: Use only with guardian consent, confirm retention and deletion terms, and avoid submitting unnecessary or sensitive media.

Risk: The skill silently creates or reuses a persistent identity and tokens for report association.

Mitigation: Review local workspace storage and publisher account controls before deployment, and provide a clear process to delete stored identities, tokens, videos, and reports.

Risk: Alerts are auxiliary visual monitoring signals and may be incomplete or incorrect.

Mitigation: Keep adult supervision in the workflow and treat alerts as prompts to check the infant rather than as medical or safety determinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with alert details and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a user-specified file; history queries are returned from the publisher cloud service.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
