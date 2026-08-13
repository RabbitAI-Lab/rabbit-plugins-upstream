## Description:

Bidding Compliance Guard screens Chinese bidding, tender, qualification, award notice, business response, and public-facing company text for high-frequency compliance-risk wording, then returns severity-ranked findings and remediation suggestions locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen bidding documents, tender announcements, qualification materials, award notices, business responses, and related public text before release or submission. It is a local compliance aid for common risky wording and does not replace professional legal or procurement compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides wording-level compliance indicators rather than legal advice or a final compliance conclusion.

Mitigation: Use results as a screening aid and have project-specific bidding materials reviewed by qualified legal or procurement compliance professionals.

Risk: Keyword and substring matching can produce false positives for negated statements and can miss risks expressed with unfamiliar phrasing.

Mitigation: Review flagged text in context, verify clean results manually for high-stakes submissions, and treat the output as one input to broader compliance review.

Risk: The security guidance states that the documented --file example is not supported by the current script.

Mitigation: Use --text or --stdin for local screening until file-input documentation and implementation are aligned.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wwumit/skills/bidding-compliance-guard)
- [Publisher profile](https://clawhub.ai/user/wwumit)
- [Artifact README](artifact/README.md)
- [Artifact skill manifest](artifact/SKILL.md)
- [Artifact changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON findings with decision, risk level, categories, matched terms, source offsets, and remediation suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local screening only; no network, credential, persistence, or destructive behavior is reported by the security evidence.]

## Skill Version(s):

1.0.0 (source: server release evidence, frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
