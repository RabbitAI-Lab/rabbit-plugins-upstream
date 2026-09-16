## Description:

Checks payroll payable ledgers locally for row arithmetic, total-row consistency, duplicate periods, blank fields, and source-cited findings within the free-version scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and bookkeeping staff use this skill during monthly closing, reconciliation, or payroll payable review to check whether payroll payable ledger rows and totals reconcile. The free version reports only the checks implemented in the bundled local engine and withholds five listed checks for the paid version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a prompt and links that steer users toward an unpinned npx installation and a paid-skill purchase flow.

Mitigation: Do not run the pasted purchase prompt or npx command unless intentionally buying the paid product, after verifying the package source, exact version, and downstream skill terms.

Risk: The free checker omits five payroll-payable checks, so users could over-read the result as a complete audit.

Mitigation: Treat results as limited to the six executed checks and review the withheld-check list before relying on the output.

Risk: The tool checks ledger arithmetic and reconciliation only; it does not validate payroll, tax, social insurance, or accounting-policy correctness.

Mitigation: Use the output as a scoped reconciliation aid and review payroll-policy, tax, and social-insurance judgments separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-payable-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, analysis, shell commands, guidance]

**Output Format:** [Plain text or JSON result reports with cited findings, executed-check scope, withheld-check list, and exit codes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs with Node.js against local text or JSON input; the wrapper states no network use, no API key, and no registration for the free checker.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
