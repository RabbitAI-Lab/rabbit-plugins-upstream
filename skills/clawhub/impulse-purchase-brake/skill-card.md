## Description:

Impulse Purchase Brake helps users evaluate supermarket and online shopping promotions by quantifying filler spending, identifying nonessential items, and prompting a pause before checkout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangyang7-star-jpg](https://clawhub.ai/user/yangyang7-star-jpg)

### License/Terms of Use:

MIT-0

## Use Case:

External consumers use this skill when they are deciding whether to buy items during supermarket or online promotions. It asks for cart items, promotion rules, and approximate remaining spending money, then produces a grounded recommendation about what to keep or remove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share more personal budget information than needed for a shopping decision.

Mitigation: Ask only for approximate remaining spending money and cart or promotion details; avoid collecting account, income, or full budget data.

Risk: Persuasive shopping advice may feel overly forceful if the user has already made a deliberate choice.

Mitigation: Keep the tone firm but nonjudgmental, base conclusions only on user-provided facts, and stop persuading if the user decides to buy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangyang7-star-jpg/skills/impulse-purchase-brake)
- [Server-resolved GitHub source](https://github.com/Yangyang7-star-jpg/skills/tree/main/impulse-purchase-brake)
- [Publisher profile](https://clawhub.ai/user/yangyang7-star-jpg)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown shopping-decision analysis with tables, lists, and short persuasive prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided cart items, promotion rules, and approximate remaining spending money; no API calls, shell commands, or code output.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
