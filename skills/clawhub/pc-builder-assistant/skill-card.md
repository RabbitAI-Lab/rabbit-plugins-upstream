## Description:

Helps plan desktop PC builds and upgrades with component recommendations, compatibility checks, and China-market price references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

People planning or upgrading desktop PCs use this skill to compare components, check build compatibility, and estimate costs for gaming, creative work, and local AI workloads.

### Deployment Geography for Use:

Global; bundled prices and hardware catalog focus on the China market.

## Known Risks and Mitigations:

Risk: China-market prices may be stale or differ from local retail prices.

Mitigation: Verify current local prices and exact product variants before purchasing; use bundled prices as planning references.

Risk: Estimated gaming performance may differ from actual results.

Mitigation: Treat FPS estimates as planning references and check current benchmarks for the chosen hardware and settings.

Risk: User-supplied catalog overlays or output paths can expose or change unintended files.

Mitigation: Provide only overlay files and output paths that you intentionally want the agent to read or write.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility guidance](references/compatibility.md)
- [Pricing guidance](references/pricing.md)
- [Local model sizing guidance](references/local-model-fit.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown build lists and explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dated price estimates and compatibility caveats when recommending specific parts.]

## Skill Version(s):

0.1.42 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
