## Description:

Deterministic legal compliance verification for cosmetic formulations against EU CosIng regulations. Resolves trade names to INCI standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[boriskuncer](https://clawhub.ai/user/boriskuncer)

### License/Terms of Use:

MIT-0

## Use Case:

Cosmetic formulators, regulatory reviewers, and agents evaluating EU market access use this skill to check ingredient lists for EU CosIng restrictions, concentration limits, and product category constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Formulation ingredients and payment transaction signatures are sent to an external endpoint.

Mitigation: Install only if that data sharing is acceptable for the intended formulations and payment workflow.

Risk: Compliance results may be incomplete or unsuitable as the sole basis for regulatory decisions.

Mitigation: Use the skill as a compliance aid and have qualified regulatory reviewers confirm market access decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/boriskuncer/skills/complicheck-skill)
- [Publisher Profile](https://clawhub.ai/user/boriskuncer)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill describes a paid HTTP API call that returns structured ingredient compliance results.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
