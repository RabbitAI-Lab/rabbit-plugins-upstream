## Description:

Highlights risky phrases in Chinese ad copy with source line numbers and legal basis for absolute terms, medical and cosmetic claims, education guarantees, investment and real-estate promises, false-efficacy promises, and missing mandatory notices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as e-commerce operators, brand marketers, and ad buyers use this skill to screen Chinese advertising copy before publication. It flags mechanically detectable compliance issues and returns line-level findings, legal basis, and review guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Users may treat the compliance report as legal advice or as a final platform approval decision.

Mitigation: Present results as a screening aid and require human legal or policy review before publication or enforcement decisions.

Risk: Broad trigger terms may cause this skill to be suggested for general advertising-policy complaints outside its intended scope.

Mitigation: Use it for Chinese or Mainland-China advertising-copy compliance screening, and route unrelated policy or legal questions to appropriate review.

Risk: Mechanical phrase matching may miss context or flag legitimate quotations, comparative claims, or industry-specific material.

Mitigation: Review each finding against the full advertisement, supporting evidence, and applicable platform or regulatory requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ad-copy-rewrite-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON compliance report with findings, source line numbers, legal basis, and advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and reports withheld checks and insufficient-input cases instead of filling defaults.]

## Skill Version(s):

1.0.62 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
