## Description:

Helps users plan desktop PC builds and upgrades, compare components, check compatibility, and estimate costs for gaming, creative work, and local AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

People planning a desktop PC build or upgrade use this skill to select parts within a budget, check fit and compatibility, and understand price and performance trade-offs. It also advises on gaming frame rates and GPU and memory sizing for local AI workloads.

### Deployment Geography for Use:

Global; bundled price references are for the China market in CNY, with user-provided local-currency overlays supported.

## Known Risks and Mitigations:

Risk: Bundled China-market prices or catalog entries may be stale or incomplete, leading to misleading purchase estimates.

Mitigation: Check current retailer listings and exact vendor specifications before an expensive purchase; keep local-currency overlay prices separate from CNY references.

Risk: Game frame-rate predictions may be mistaken for measured benchmark guarantees.

Mitigation: Treat FPS figures as estimates based on listed samples, not guaranteed results.

Risk: Some case entries, particularly NAS- or server-looking models, may not suit a desktop build.

Mitigation: Verify the intended case type, dimensions, and component clearance against vendor specifications before buying.

Risk: User-supplied local catalog overlay files may contain information the user did not intend to share.

Mitigation: Provide only overlay files you trust and intend the assistant to read.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility guidance](references/compatibility.md)
- [Pricing guidance](references/pricing.md)
- [Gaming performance guidance](references/game-performance.md)
- [Local model fit guidance](references/local-model-fit.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Natural-language recommendations and Markdown component lists with prices and compatibility notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes include reference dates; complete builds include itemized parts, totals, trade-offs, and checks to perform before buying.]

## Skill Version(s):

0.1.43 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
