## Description:

收款手续费核对（免费）逐项复算收款手续费核对表，并为每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users use this skill to check payment-fee worksheets for recalculation errors, total-row mismatches, duplicate channels, and blank or placeholder fields. It is intended for local review of copied worksheet text, with insufficient input reported instead of inferred conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill embeds a paid-upgrade flow that asks an assistant to run unpinned remote package code and delegate to newly installed instructions.

Mitigation: Use the free local checker only after reviewing the bundled Node script, and do not let an agent run the unpinned `npx ... @latest` command or start purchase steps automatically.

Risk: Payment-fee conclusions can be misleading when worksheet text lacks required headers or rows.

Mitigation: Provide copied worksheet text with the required headers and review any insufficient-input response instead of treating it as a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payment-fee-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis with source line references and local Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed free checks, withheld checks, summary counts, missing input requirements, and whether network use occurred.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
