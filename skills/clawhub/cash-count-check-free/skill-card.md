## Description:

Checks cash count tables for arithmetic consistency, total rows, duplicate shifts, blanks, and cash overage or shortage sign/type mismatches, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators, cashiers, and finance reviewers use this skill to check copied cash count tables for shift-level cash overage and shortage calculation issues before operational follow-up. It provides arithmetic validation and missing-data feedback, not audit, legal, or fraud determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text steers users or agents toward installing an unpinned payment package and buying a separate paid skill.

Mitigation: Use the local checker only when it fits the task; do not run the purchase or install command unless the package, source, version, and product have been independently verified.

Risk: External purchase or payment confirmation could be initiated outside the free checker workflow.

Mitigation: Keep payment confirmation manual and run any external install steps in a constrained environment.

Risk: The free checker reports only its included checks and lists withheld checks that were not executed.

Mitigation: Treat results as arithmetic validation for the stated free checks and review withheld or out-of-scope checks before relying on the result operationally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cash-count-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing findings, summaries, executed checks, withheld checks, and insufficient-input messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each finding cites source line context when checks run; the free tier lists checks that were not executed.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
