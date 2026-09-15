## Description:

A free local checker that compares supplied trade documents for cross-document inconsistencies in key identifiers, amounts, quantities, weights, ports, vessel names, shipping marks, and leftover template placeholders, with evidence for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trade operations teams use this skill before document submission to check whether invoices, packing lists, bills of lading, and related trade documents disagree on core fields. The skill is a scoped consistency screen and does not determine whether a bank will accept the documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade path asks an agent to run an unpinned remote installer and then follow instructions from newly installed external content.

Mitigation: Treat the paid-upgrade flow as a separate trust decision: verify the package source and exact version, avoid `@latest`, and require human review before following newly installed instructions.

Risk: The optional upgrade path includes wallet or payment steps.

Mitigation: Do not allow an agent to approve wallet authorization or payment; require the user to inspect and confirm any payment link or QR code directly.

Risk: Users may over-read a clean result because the free checker intentionally omits several document checks and does not judge bank acceptance.

Mitigation: Use the output as a limited consistency screen for the listed checks only, and review omitted checks and bank or credit terms separately before relying on the documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/trade-doc-consistency-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance, shell commands]

**Output Format:** [Human-readable text or JSON containing consistency findings, cited source snippets, omitted checks, status, and advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied input and reports insufficient input without making a consistency conclusion.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
