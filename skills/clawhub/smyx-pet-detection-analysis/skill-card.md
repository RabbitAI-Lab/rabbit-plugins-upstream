## Description:

Detects cats, dogs, and birds in images or video streams for home pet monitoring and returns structured detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home monitoring images or videos for cats, dogs, and birds, then receive structured results, report links, or historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household monitoring images, videos, identifiers, and account-scoped report history may be sent to cloud services.

Mitigation: Use only with explicit user consent for cloud processing, document identity creation and token handling, and disclose historical report retrieval behavior before deployment.

Risk: Default or development configuration may use plaintext HTTP for media, identifiers, or tokens despite documentation that claims HTTPS transport.

Mitigation: Remove development HTTP configuration, enforce HTTPS-only allowlisted hosts, and verify transport settings before running the skill with real media.

Risk: Historical report retrieval can expose prior pet-monitoring reports linked to the current account identity.

Mitigation: Require explicit confirmation before fetching historical reports and show only the minimum report details needed for the user request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet detection API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis output, with optional Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured detection counts, confidence-threshold-dependent results, report links, and saved output files when requested.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
