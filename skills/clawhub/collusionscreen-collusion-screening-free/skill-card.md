## Description:

Screens multiple bid documents locally for objective, reproducible collusion clues, limited in the free version to shared contact details and overlapping project personnel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement reviewers, bidding teams, and agents use this skill to compare multiple bidders' documents for repeated contact details and overlapping project personnel. It surfaces reproducible clues for human review and does not make final bid-rigging determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes an optional paid upgrade flow that asks an agent to run unpinned remote installer code and initiate a purchase.

Mitigation: Do not run the optional SkillPay or npx purchase instructions unless the user intentionally wants the paid product, has verified the package and publisher, and personally confirms any wallet authorization or payment.

Risk: Screening output could be mistaken for a legal or bid-evaluation conclusion.

Mitigation: Treat the output as objective clues for review; final determinations should remain with the relevant evaluation committee, regulator, or qualified human reviewer.

Risk: The free version omits several advertised checks, including text similarity, pricing patterns, mixed files, repeated errors, guarantee source, and format fingerprint checks.

Mitigation: Review the reported checks_given and checks_withheld fields and do not infer that omitted checks were performed.

Risk: Bid documents may contain sensitive commercial or personal information.

Mitigation: Run the tool locally as documented, avoid unnecessary sharing of inputs or outputs, and keep masked findings tied to authorized review workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/collusionscreen-collusion-screening-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; outputs masked findings and lists executed and withheld checks.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
