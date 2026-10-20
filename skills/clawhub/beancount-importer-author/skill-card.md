## Description:

Write or repair a reusable Beangulp importer from a sample bank export for a local ledger, with reviewed golden files and a passing test harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining local Beancount ledgers use this skill to create or repair tested Python/Beangulp importers for bank export formats and connect a confirmed importer to their runner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted-account tools or cloud cloning could expose financial data or extend the workflow beyond local importer authoring.

Mitigation: Keep this workflow local-only; exclude hosted-account tools and cloud cloning.

Risk: Bank export samples saved as fixtures may expose sensitive financial information.

Mitigation: Redact bank samples before saving or committing test fixtures.

Risk: Generated importer output or runner changes could be incorrect, and live ledger changes could occur without appropriate authorization.

Mitigation: Review generated outputs and the runner diff, and authorize any live ledger changes separately.

## Reference(s):

- [Beangulp API guide](references/beangulp-api.md)
- [bea CLI guide](references/bea-cli.md)
- [bea import guide](references/bea-import.md)
- [Compatibility guide](references/compatibility.md)
- [Deduplication guide](references/dedup.md)
- [Skill source homepage](https://github.com/bex-co/beancount-io/tree/main/skills)
- [ClawHub skill page](https://clawhub.ai/puncsky/skills/beancount-importer-author)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Python importer files, golden-file test fixtures, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Importer wiring is confirmation-gated; generated outputs and test fixtures require review.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
