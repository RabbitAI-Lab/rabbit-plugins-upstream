## Description:

Return earning rates, caps, exclusions, activation requirements, and merchant-coding caveats for one major-US credit card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to get an earn-side breakdown for one exact major U.S. credit card, including rates, category caps, exclusions, activation requirements, and merchant-coding caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use web search or WebFetch for credit-card earning structures.

Mitigation: Do not provide bank account access, credentials, browser profiles, or local private files; the skill should only need public card information.

Risk: Credit-card earning rates, caps, exclusions, and activation requirements can change or vary by exact card variant.

Mitigation: Resolve the exact card variant, prefer the issuer page first, and include confidence notes when terms are unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiahongc/skills/card-rate)
- [jiahongc publisher profile](https://clawhub.ai/user/jiahongc)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown sections with hidden YAML sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issuer-first web research with confidence notes; no executable code or persistence.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
