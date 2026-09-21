## Description:

Plans Amazon A+ content modules, information hierarchy, and buyer-question responses from product-detail and review evidence, and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace content operators and ecommerce teams use this skill to plan Amazon A+ content from product details and review evidence before drafting or updating product pages. It supports planning only and does not run ads, create images, or publish Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the CLI can run broader server-side workflows than the advertised fixed A+ content-planning scope.

Mitigation: Use only the documented listing/aplus operations flow, and approve operations run commands only when workflow/focus and requestId match the reviewed quote.

Risk: The skill requires an ARI API key and can trigger paid collection or analysis actions.

Mitigation: Use only an ARI account the user is comfortable authorizing, run quote before paid actions, and require explicit user confirmation before any command with --confirm.

Risk: Planning outputs are based on available product-detail and review evidence and may omit real-time store, inventory, advertising, order, profit, or pricing facts.

Mitigation: State evidence gaps plainly and have a human reviewer verify claims before using the plan in customer-facing Amazon content.

## Reference(s):

- [Amazon A+ Content Planning README](artifact/README.md)
- [Amazon A+ Content Planning Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon A+ Content Planning API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or concise text with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection or analysis actions require quote review and explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: evidence.release.version, artifact/_meta.json, artifact/CHANGELOG.md, artifact/scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
