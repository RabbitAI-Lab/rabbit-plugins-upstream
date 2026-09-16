## Description:

八字算命AI大师 helps Chinese-language users generate Bazi chart readings, Mei Hua Yi Shu divination, and Feng Shui self-check guidance using bundled rule-based calculators and cultural-reference disclaimers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hhyj369](https://clawhub.ai/user/hhyj369)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language users use this skill for cultural-reference Bazi readings, single-question Mei Hua divination, and home or office Feng Shui self-checks. It is not a substitute for medical, legal, financial, or other licensed professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users for birth details or personal questions for fortune-telling workflows.

Mitigation: Use it only when users are comfortable sharing the minimum details needed for the local calculator workflow, and avoid retaining those details outside the active session.

Risk: The security summary flags broad activation triggers and rigid response-control instructions.

Mitigation: Review the trigger list and scripted opening or verbatim response requirements before enabling the skill in shared or high-trust agent environments.

Risk: Fortune-telling, divination, and Feng Shui outputs may be mistaken for professional advice.

Mitigation: Keep the cultural-reference framing, disclaimers, and boundaries for medical, legal, financial, safety, and crisis topics visible in generated responses.

Risk: Bazi and Mei Hua calculations depend on the local lunar_python package.

Mitigation: Provision and test the dependency before release, and require the agent to state reduced precision when calculator execution fails.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/hhyj369/skills/real-ai-fortune)
- [README](artifact/README.md)
- [Calculation rules](artifact/calculation-rules.md)
- [Mei Hua special requirements](artifact/meihua-special-requirements.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese Markdown prose with optional local script command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-part readings with stated precision limits and cultural-reference disclaimers]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
