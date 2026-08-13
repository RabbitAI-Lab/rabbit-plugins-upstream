## Description:

Analyzes fixed-enclosure reptile feeding videos to detect prey attack, swallowing, feeding refusal, and post-feeding regurgitation or vomiting events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, vivarium operators, and developers use this skill to send feeding media to a cloud analysis service and receive structured behavior reports, alert levels, recommendations, and report links for refusal or vomiting events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud media analysis can send reptile enclosure media or supplied media URLs to the lifeemergence service.

Mitigation: Use only media suitable for external cloud processing and avoid private URLs or sensitive footage.

Risk: The skill can create or reuse an internal identifier and maintain local workspace data such as session tokens.

Mitigation: Review local SQLite/token storage before use and delete workspace data and tokens before handling sensitive footage or sharing the environment.

Risk: Visual feeding analysis can be mistaken for veterinary diagnosis.

Mitigation: Treat outputs as behavior records and consult a professional reptile veterinarian for repeated refusal, vomiting, or health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis reports, with optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links, alert levels, recommended actions, and history tables.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
