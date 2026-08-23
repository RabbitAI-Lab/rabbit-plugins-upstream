## Description:

Guides an agent to collect product facts from an operator or merchant and produce strict colon-labeled product-intro text aligned with a product cognition parser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdpb](https://clawhub.ai/user/kwdpb)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and agent builders use this skill to turn product details into a structured ai_product_intro entry for AI shopping-assistant knowledge bases. It is for intake and formatting, not direct product recommendation or price comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated product intro could contain unsupported claims, absolute language, or regulated health wording if the source product information is inaccurate.

Mitigation: Review claims before use; keep factual evidence separate from marketing claims and move prohibited wording into the disallowed-expression field.

Risk: Using the system-prompt variant in a multi-purpose agent can make the agent behave like a dedicated intake bot.

Mitigation: Use SKILL.md for multi-purpose agents and reserve system-prompt.md for dedicated intake bots.

Risk: Changing labels or thresholds without updating downstream parsers can cause product entries to be skipped or misread.

Mitigation: Keep the format specification, prompt shell, and referenced parser implementations aligned whenever labels, aliases, or thresholds change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kwdpb/skills/product-cognition-intake)
- [README.md](artifact/README.md)
- [Format specification](artifact/规范.md)
- [Examples](artifact/examples.md)
- [Changelog](artifact/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text with strict colon-labeled lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be copied into a product intro or ai_product_intro field after human review.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
