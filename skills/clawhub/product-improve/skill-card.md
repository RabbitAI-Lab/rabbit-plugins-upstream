## Description:

This skill helps Amazon sellers turn ARI-collected review complaints into prioritized product-improvement actions, including material, packaging, instructions, listing, competitor, and monitoring follow-up recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to analyze product reviews, identify repeated complaints and quality issues, compare competitors, and convert evidence into prioritized product iteration work. It also guides account authorization, credit-aware report generation, ongoing review monitoring, and exports through ARI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits automatically when account auto-confirm rules allow paid collection or analysis.

Mitigation: Set auto-confirm to always ask or use quote-only flows when every charge should require approval.

Risk: The skill requires an ARI account key and can change account confirmation settings or monitoring state.

Mitigation: Authorize only the intended ARI account, keep the key out of chat and reports, and confirm autoconfirm or schedule changes before execution.

Risk: Custom ARI_BASE_URL settings could redirect authenticated ARI requests away from the official service.

Mitigation: Leave custom ARI base URLs unset unless using a controlled development server and explicitly approving that environment.

Risk: Exports can write local CSV, Markdown, or HTML files.

Mitigation: Use default export filenames or a known safe output directory and review generated files before sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-improve)
- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant User Guide](使用说明.md)
- [ARI Product Management](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with optional JSON CLI results, shell command snippets, CSV exports, and Markdown or HTML report exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key for authenticated workflows and may create local export files when export commands are used.]

## Skill Version(s):

1.4.8 (source: server release, frontmatter, _meta.json, script constant, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
