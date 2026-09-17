## Description:

Checks AP factoring and discounting tables by recalculating row formulas, validating totals, and flagging duplicate, blank, placeholder, or negative amount entries with source-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts payable teams use this skill during month-end close, reconciliation, and inventory review to check AP factoring and discounting tables before downstream accounting work. It performs the free local checks declared by the package and lists checks that were not run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid-upgrade instructions ask users to run an unpinned remote installer and start an external purchase workflow through an AI agent.

Mitigation: Do not copy the preauthorized purchase prompt or run the npx @latest installer until the package, source, payment workflow, and installed skill instructions have been independently verified.

Risk: The free checker reports only the included local checks and explicitly withholds additional factoring checks.

Mitigation: Review the checks_not_run or withheld-checks list before relying on a clean result, and treat the output as a reconciliation aid rather than complete financial assurance.

Risk: The checker operates on financial table data supplied by the user.

Mitigation: Run the local Node.js checker only in an environment where the user is comfortable processing that input file.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/ap-factoring-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or JSON report with findings, executed checks, withheld checks, scope, and summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; materials are read from user-provided table text or JSON input.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
