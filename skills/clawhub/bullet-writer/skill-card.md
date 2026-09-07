## Description:

Analyzes Amazon product details and review evidence to recommend improvements for product bullet points, limited to bullet diagnosis and suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and e-commerce operators use this skill to turn product details and ARI-collected review evidence into bullet-point listing recommendations, including selling-point gaps, buyer questions, wording issues, and supporting review evidence. It is not intended for title rewriting, advertising bidding, automatic Amazon page publication, or unsupported real-time business metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The public bullet-writing positioning under-discloses broader paid, account-changing, monitoring, advertising-keyword, and export behavior.

Mitigation: Review the ARI API-key storage, billing confirmation settings, scheduled collection and watch behavior, export paths, and any account-state-changing actions before installation or execution.

Risk: Some workflows can consume credits or change account settings through confirmation or server-managed auto-confirm behavior.

Mitigation: Use quote-only flows when pricing is requested, confirm costs before chargeable actions, and review auto-confirm settings before allowing recurring or account-affecting work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bullet-writer)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Dedicated listing bullets workflow](artifact/references/operation-workflow.md)
- [User guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Natural-language guidance and Markdown reports, with JSON CLI responses and optional CSV, Markdown, or HTML export files when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid, monitoring, export, and account-setting actions follow the documented confirmation or server-managed auto-confirm flow.]

## Skill Version(s):

1.4.7 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
