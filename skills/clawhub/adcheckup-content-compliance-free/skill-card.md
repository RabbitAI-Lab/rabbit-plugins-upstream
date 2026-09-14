## Description:

A free local pre-check that scans Chinese advertising copy for absolute terms and reports limited Advertising Law guidance-based findings and exemptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and content reviewers use this skill before publication to mechanically screen Chinese advertising copy for absolute-term claims and to see which matched phrases are treated as exempt. It is a limited pre-check and does not replace legal review or regulator determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the mechanical output as legal advice or a complete advertising-law review.

Mitigation: State that results are a limited pre-check and require legal or regulatory review for final determinations.

Risk: The free release excludes broader sensitive-word, medical, finance, education, real-estate, and bulk checks.

Mitigation: Show withheld checks alongside results so users know which review areas were not executed.

Risk: Incomplete or malformed input can lead to misleading confidence if the skill returns a conclusion.

Mitigation: Report insufficient input and avoid producing a compliance conclusion when required copy is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/adcheckup-content-compliance-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Human-readable text or JSON with executed checks, withheld checks, findings, exemptions, and notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided copy; reports insufficient input instead of producing a compliance conclusion.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
