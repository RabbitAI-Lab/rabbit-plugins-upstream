## Description:

A free local contract consistency checker that reports recomputable evidence for party-name, date, amount, placeholder, clause-reference, and defined-term issues without registration, payment, API keys, or network use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run local pre-signature contract consistency checks and receive evidence-backed findings for mechanical contradictions. It supports review preparation, not legal advice or a complete contract assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical consistency findings as legal advice or a complete contract review.

Mitigation: Use the output as evidence-backed consistency checks and have qualified reviewers assess legal, commercial, and omitted issue areas.

Risk: The optional website mentioned in the documentation is separate from the local no-network workflow.

Mitigation: Keep sensitive contracts in the local Node workflow unless the external website's handling is separately reviewed and approved.

Risk: A clean result can be mistaken for an all-clear on the whole contract.

Mitigation: Review the listed checks performed and checks withheld; treat clean results as limited to the included consistency checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/contract-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with line-level evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only execution; insufficient input returns no consistency conclusion.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
