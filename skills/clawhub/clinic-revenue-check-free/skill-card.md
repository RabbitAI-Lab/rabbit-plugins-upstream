## Description:

Checks clinic medical revenue and insurance settlement tables for row arithmetic, total reconciliation, duplicate batches, missing fields, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Clinic and private-hospital finance staff use this skill during monthly close, reconciliation, or inventory checks to review medical revenue and insurance settlement tables before follow-up with insurers or internal accounting teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker documentation and default output point users toward an external paid install and purchase workflow using an unpinned npm command.

Mitigation: Do not run the optional paid-upgrade command or begin the purchase workflow unless the external package, merchant, and payment flow have been separately reviewed and trusted.

Risk: The checker reads user-supplied settlement tables, which may contain sensitive financial or healthcare-related data.

Mitigation: Run it only in a trusted local environment and avoid sharing inputs or outputs outside approved accounting or compliance workflows.

Risk: The free version omits several policy and reference-threshold checks, so a clean result is not a full settlement audit.

Mitigation: Treat results as deterministic checks for the listed free checks only, and review omitted or out-of-scope issues against local医保 policy, contracts, and settlement records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/clinic-revenue-check-free)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings, with local shell commands for running the checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs as a local Node.js script over user-supplied JSON or pasted tabular text; sample input is included.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
