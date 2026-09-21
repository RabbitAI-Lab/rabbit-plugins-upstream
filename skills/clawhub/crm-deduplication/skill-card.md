## Description:

Audits CRM account identity, builds a disabled deduplication play, merges only safe exact LinkedIn company ID matches, and routes uncertain clusters to Slack-based human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations teams and developers use this skill to set up guarded CRM account deduplication in a Cargo CDK project. It helps audit duplicate candidates, configure a disabled merge-capable play, require approvals, and report verified CRM outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow has real CRM merge authority and can change customer account records during a pilot.

Mitigation: Keep the play disabled, require separate disabled-build and pilot approvals, limit the pilot to 15 rows, and verify every survivor and absorbed child ID after a merge.

Risk: Stale duplicate evidence can cause a merge decision to use records that changed after the audit.

Mitigation: Search the live CRM during each run, avoid connector caching, stop if the source row is missing or changed, and refresh schemas, costs, and population before pilot approval.

Risk: Ambiguous duplicate candidates can represent distinct companies, parent-subsidiary relationships, or records with conflicting protected identifiers.

Mitigation: Limit unattended merges to exact shared LinkedIn company ID without conflicts and route all other candidates to Human Review through the approved Slack destination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/crm-deduplication)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Audit CRM account duplicates](references/audit.md)
- [Configure CRM deduplication](references/configure.md)
- [Run CRM deduplication](references/run.md)
- [Acceptance checklist](evals/acceptance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON audit and report contracts, TypeScript CDK examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires operator approvals before deployment and before any merge-capable pilot; the checked play remains disabled, serial, and limited to 15 rows.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
