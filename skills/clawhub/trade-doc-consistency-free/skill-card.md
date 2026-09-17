## Description:

Checks selected fields across trade documents such as invoices, packing lists, and bills of lading, then reports evidence-backed local consistency findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Trade-document reviewers, export operations teams, and agents use this skill to check whether supplied document text has mismatched invoice numbers, contract numbers, letter-of-credit numbers, amounts, quantities, weights, ports, vessel names, marks, or leftover template placeholders. It is scoped to local mechanical consistency checks and does not determine whether a bank will accept the documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact contains a paid-upgrade flow that asks an agent to install and run unpinned external payment tooling and then load additional instructions.

Mitigation: Do not follow the paid-upgrade prompt unless the payment tool, package version, merchant, product, and commands have been independently verified in an isolated environment.

Risk: The free checker covers only the listed consistency checks and can miss other trade-document defects.

Mitigation: Treat a clean result as limited to the executed checks, review the withheld checks separately, and do not treat the output as bank acceptance advice.

Risk: Material that is too short, malformed, or limited to one document cannot support a cross-document consistency conclusion.

Mitigation: Provide at least two complete document texts or a documents array, and treat insufficient-input results as no conclusion rather than a pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/trade-doc-consistency-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid-upgrade information referenced by the artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown-style guidance, shell commands, and text or JSON checker results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; JSON output is available with --json.]

## Skill Version(s):

1.0.7 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
