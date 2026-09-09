## Description:

Analyzes ARI-collected Amazon review data across products and competitors to identify rival strengths, recurring pain points, differentiation opportunities, and operating recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to ask an agent for competitor review comparisons, pain point summaries, trend checks, listing suggestions, and exported reports based on ARI-collected Amazon review data.

### Deployment Geography for Use:

Global, limited to supported Amazon marketplaces documented by the skill.

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits when service auto-confirm rules allow paid analysis to run without a fresh prompt.

Mitigation: Before paid use, set autoconfirm off or ask for quote-only operation; when confirmation is required, proceed only after the user accepts the quoted credits.

Risk: The skill connects to an ARI account and stores a local API key.

Mitigation: Use the browser authorization flow or local hidden input, never ask the user to paste secrets into chat, and guide the user to regenerate the key after authentication failures.

Risk: Monitoring, schedules, competitor binding, or confirmation settings can affect future collection behavior and costs.

Mitigation: Treat these as explicit account changes: report the schedule or watch cost, require user intent before changing them, and review current schedules or watches before enabling recurring collection.

Risk: Amazon review conclusions can be misleading when ARI has limited samples, narrow collection windows, or incomplete variant coverage.

Mitigation: State the sample count, time window, marketplace, and known coverage limits; avoid presenting unsupported trends or variant-level findings as definitive.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/funewa/skills/competitor-review)
- [User guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or concise text with optional shell commands, links, CSV/Markdown/HTML export guidance, and JSON-backed API results summarized for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state data scope, sample limits, credit usage, and report links when available.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, CHANGELOG, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
