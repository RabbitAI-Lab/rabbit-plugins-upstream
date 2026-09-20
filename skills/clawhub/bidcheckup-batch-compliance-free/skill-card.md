## Description:

Checks line-item bid arithmetic across multiple bidders in one local pass and reports per-bidder issues without registration, payment, or API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement reviewers use this skill to pre-check bidder line-item arithmetic before formal review. It helps identify mismatched quantity, unit price, and amount values while leaving bid evaluation decisions to the responsible reviewers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the arithmetic check as a formal bid evaluation or assume it covers omitted compliance checks.

Mitigation: Review results manually, keep bid files local, and use the output only for line-item arithmetic checking unless separate evidence supports broader review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bidcheckup-batch-compliance-free)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON summaries with per-bidder verdicts and findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, insufficient-input cases, and local execution scope.]

## Skill Version(s):

1.0.51 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
