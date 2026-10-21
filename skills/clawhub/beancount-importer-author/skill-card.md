## Description:

Author or repair a reusable Beangulp importer from a sample bank export, with reviewed golden files and a passing test harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers use this skill to create or repair a tested Python Beangulp importer for a local Beancount ledger from a bank export, including reviewed golden-file tests and guidance for wiring a confirmed runner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real bank exports and generated golden files may contain private financial information that could be exposed through version history or sharing.

Mitigation: Use sanitized or synthetic samples, inspect both samples and generated goldens, and remove sensitive data before committing or sharing tests.

Risk: The documented hosted-ledger fallback conflicts with the stated local-only scope and could lead to unintended remote ledger access.

Mitigation: Resolve the scope conflict before allowing hosted-ledger access; keep use local until that fallback is explicitly reviewed and approved.

## Reference(s):

- [Beangulp API reference](references/beangulp-api.md)
- [Bea CLI reference](references/bea-cli.md)
- [Importer compatibility reference](references/compatibility.md)
- [Bea import reference](references/bea-import.md)
- [Deduplication reference](references/dedup.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Guidance]

**Output Format:** [Python importer code, golden-file test files, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the supplied bank export and confirmed target account; review generated samples and tests before sharing or committing.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
