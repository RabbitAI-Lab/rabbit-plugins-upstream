## Description:

A local checker for tax self-review worksheets that runs five built-in checks per client directory and prints one conclusion line per client with source file and line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External tax and accounting staff use this skill after filings and before tax self-review or annual reconciliation to run local arithmetic and consistency checks across client tax materials. It is a checking aid, not tax advice, legal assurance, filing automation, or a replacement for review by a qualified tax professional or tax authority.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill reads local tax material from the path supplied with --input.

Mitigation: Run it only against intended client directories or files, and avoid passing broader folders than needed.

Risk: Results may be mistaken for tax advice or legal assurance.

Mitigation: Treat output as arithmetic and consistency checks only, and have qualified tax staff or the relevant authority review tax positions.

Risk: A clean result can hide checks that were not executed because materials were missing, unrecognized, or outside the free version.

Mitigation: Review the skill's unexecuted and withheld check listings before relying on any conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-risk-benefit-pack-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON printed to stdout; documentation includes Markdown command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library behavior described by the artifact; reads user-provided tax material paths and does not write output files.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
