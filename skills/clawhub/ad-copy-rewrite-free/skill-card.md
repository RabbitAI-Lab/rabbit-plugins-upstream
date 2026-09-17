## Description:

Screens Chinese advertising copy for mechanically detectable compliance risks and returns line-level findings with matched terms, legal basis, and review advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, and agents use this skill to check Chinese ad headlines, product descriptions, scripts, and labels before publication. It flags absolute claims, medical and cosmetic claims, education guarantees, investment and real-estate promises, false efficacy promises, and missing mandatory notices.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill includes optional paid upgrade, installation, and purchase instructions that could lead an agent toward follow-on installation or payment steps.

Mitigation: Review the paid flow manually; do not allow an agent to run the optional npx command, install follow-on skills, or start a purchase unless the SkillPay source is independently trusted and payment is confirmed by the user.

Risk: The checker provides mechanical screening for Chinese advertising-law text patterns and may miss context, platform rules, factual substantiation, visual claims, or industry approval requirements.

Mitigation: Use the output as pre-publication screening only, and require human compliance or legal review before relying on results for publication decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ad-copy-rewrite-free)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Human-readable text or JSON with summary, findings, exempted phrases, scope, and disclaimer fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; insufficient input returns an insufficient_input status rather than a clean compliance verdict.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
