## Description:

Extracts packaging improvement tasks and supporting evidence from Amazon review feedback about damage, missing parts, unboxing, and storage, and is limited to packaging issue analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn ARI-collected reviews for a product ASIN into packaging-focused findings, evidence, and operational improvement tasks. It is not intended for logistics claims, supplier ordering, purchasing execution, inventory accounting, or order accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account-connected workflows beyond packaging-only analysis, including paid report generation, exports, monitoring setup, competitor binding, and billing confirmation settings.

Mitigation: Install and use it only for an ARI account where those operations are intended, and keep autoconfirm set to always ask unless the account owner explicitly wants automatic confirmation.

Risk: ARI API keys grant account access for review operations.

Mitigation: Use the browser authorization or local hidden-input setup flow, do not paste keys into chat or reports, and revoke or recreate keys from the ARI account page if access should change.

Risk: A paid command can be interrupted after the service has already charged credits and archived a report.

Mitigation: Check the latest report or operation status before retrying any confirmed paid command.

Risk: Packaging conclusions depend on the ARI-collected review sample and may not cover every Amazon review or variant.

Mitigation: State the sample size, site, data window, and coverage limits, and treat small-sample results as directional.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/packaging-improve)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [Packaging Operations Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and structured JSON from ARI CLI responses, with occasional shell commands for setup or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report URLs, credit usage, data ranges, and exported CSV, Markdown, or HTML files when the user requests export.]

## Skill Version(s):

1.4.8 (source: server release, artifact frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
