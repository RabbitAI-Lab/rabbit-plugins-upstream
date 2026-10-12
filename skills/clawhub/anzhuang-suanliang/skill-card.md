## Description:

Generates preliminary installation-works quantity schedules and materials plans from DWG drawings or existing scan indexes, with review lists for uncertain estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Construction estimators and MEP engineers use this skill to prepare preliminary quantity takeoffs and procurement plans from installation drawings, and to cross-check them against drawings and specialist software. Its estimates are not final measurements, settlement quantities, or pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically download, install, and execute a persistent external CAD-reader dependency during use.

Mitigation: Review the dependency before use in restricted environments; preferably preinstall a trusted cad-file-reader and point CAD_SKILL_DIR to it, or disable automatic setup with SKILL_NO_BASE=1 or CAD_AUTO_SETUP=0 where appropriate.

Risk: Drawing-based estimates can omit vertical runs or misclassify ambiguous circuit and equipment annotations.

Mitigation: Review unmatched items, confidence flags, and exclusions against the drawings and specialist software before procurement or other consequential use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Skill documentation](artifact/README.md)
- [Calculation rules and scope](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Spreadsheet files, JSON scan indexes]

**Output Format:** [Multi-sheet XLSX workbook and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities, material allowances, confidence indicators, and items requiring manual review; no prices or final settlement quantities.]

## Skill Version(s):

1.0.3 (source: ClawHub release; bundled files identify their internal version as 0.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
