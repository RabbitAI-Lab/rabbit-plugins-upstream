## Description:

A free local quote-audit skill that checks bid quote line items for arithmetic mismatches and missing quantity, unit price, or total fields without requiring payment, registration, or an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to pre-check bidding quote material before submission by finding line-item arithmetic errors and incomplete quote fields. It is a mechanical audit aid and does not provide bid evaluation decisions, scoring, or legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation asks users to run an unpinned external payment installer and follow newly installed instructions for a paid upgrade.

Mitigation: Treat the paid-upgrade path as a separate high-trust action; independently verify the package, source, version, payment flow, and merchant details before running the installer or installing another skill.

Risk: Users may treat a mechanical quote pre-check as an official bid evaluation or scoring decision.

Mitigation: Use the output only as an audit aid for arithmetic and missing-field checks, and keep final bid evaluation, scoring, and legal determinations with the responsible reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bidguard-quote-audit-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [analysis, text, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; returns insufficient-input status instead of conclusions when provided material cannot be parsed.]

## Skill Version(s):

1.0.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
