## Description:

Identify OEM part numbers from PDF parts catalogs by matching vehicle scope, exploded positions, and parts-table entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to identify OEM vehicle part numbers from PDF parts catalogs, including cases where a component is available only as part of a larger assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded parts-catalog PDFs can carry ordinary document-handling risk.

Mitigation: Use reputable catalog sources, keep PDF tooling up to date, and inspect only the relevant pages needed for the answer.

Risk: Catalog text extraction can misalign diagram positions, variants, sides, or assembly-only parts.

Mitigation: Confirm vehicle scope, diagram position, table row, side, quantity, and variant from the catalog before reporting a part number.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/oem-parts-catalog-identification)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with catalog citations and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final answers should cite the catalog URL and relevant PDF pages.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
