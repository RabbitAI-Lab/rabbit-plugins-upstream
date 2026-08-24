## Description:

Through fixed enclosure cameras, the skill analyzes feeding-time and post-feeding videos of reptiles to detect prey-attack behavior, successful swallowing, feeding refusal, and regurgitation or vomiting events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, and developers use this skill to analyze enclosure feeding videos or URLs for refusal, swallowing, regurgitation, signal reliability, and suggested follow-up actions. It is intended to produce behavior records and alerts, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or URLs are sent to a remote service for analysis.

Mitigation: Use the skill only with footage that can be shared with the configured service, and confirm the service endpoint and publisher are trusted before installation.

Risk: The skill may create or reuse an identity and store authentication tokens locally.

Mitigation: Run it in an isolated workspace, review token storage behavior, and remove local credentials when access is no longer needed.

Risk: Development or private-network endpoints may be present in configuration.

Mitigation: Confirm production HTTPS endpoints before use and avoid running the skill with private dev endpoints in customer or production workflows.

Risk: Feeding refusal or vomiting analysis can be mistaken for veterinary diagnosis.

Mitigation: Treat outputs as behavior observations and follow-up suggestions only; consult a qualified reptile veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis results with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include attack, swallow, regurgitation, refusal, confidence, alert level, recommended actions, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
