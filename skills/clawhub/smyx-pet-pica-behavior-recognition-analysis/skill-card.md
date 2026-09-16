## Description:

This skill analyzes indoor pet camera videos or video URLs through server-side APIs to identify pica-related mouth contact with hazardous non-food items and return warnings, risk levels, recommendations, and report links without offering medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for pet safety monitoring workflows that analyze indoor video, detect sustained contact between a pet's mouth and risky non-food objects, and produce alert-oriented reports for smart-home or camera review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor camera files or URLs may be sent to a cloud service for analysis.

Mitigation: Use only authorized pet-monitoring media, disclose cloud processing to users, and avoid submitting videos that include unnecessary private spaces or bystanders.

Risk: The skill may create or reuse a persistent identity without prompting the user.

Mitigation: Require clear consent for identity linkage, document how report history is associated with the user, and provide a way to reset or revoke the linkage.

Risk: Cloud tokens may be stored locally in plaintext and the release includes cleartext development endpoint defaults.

Mitigation: Store tokens with an appropriate secrets mechanism, use HTTPS-only production endpoints by default, and remove or gate development endpoint configurations before broad deployment.

Risk: The security guidance identifies a dependency issue involving the yaml package.

Mitigation: Use a maintained YAML dependency such as PyYAML with an explicit, valid version and verify dependency installation during release testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Pet pica behavior recognition API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured analysis reports, warning summaries, risk levels, recommendations, report links, and optional JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video paths, video URLs, pet type selection, history listing, and optional file output.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
