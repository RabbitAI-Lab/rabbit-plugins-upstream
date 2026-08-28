## Description:

Guides an agent through real-browser QA of an existing runnable web application, with optional authorized repair, release, and post-deployment regression workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liubai00](https://clawhub.ai/user/liubai00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA-focused coding agents use this skill to exercise web applications in a real browser, record durable evidence, triage defects, and, when explicitly authorized, repair issues and verify releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repair, delivery, deployment, rollback, or high-side-effect browser actions could affect real systems if authority is unclear.

Mitigation: Require explicit authorization for the target environment and each allowed action before repair or release work; keep production, delivery, rollback, and credential/session access out of scope unless specifically granted.

Risk: Browser QA can encounter sensitive sessions, credentials, or personal data while collecting evidence.

Mitigation: Use sanitized evidence references, avoid storing secrets or raw personal data, and prefer isolated non-production targets for mutable testing.

Risk: A stale or incomplete QA pass could be mistaken for release confidence.

Mitigation: Use the durable ledger, bind checks to declared scenarios and targets, and report residual untested scope instead of claiming exhaustive assurance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liubai00/skills/webapp-qa-loop)
- [Project Homepage](https://github.com/liubai00/webapp-qa-loop)
- [scope-and-selection.md](references/scope-and-selection.md)
- [browser-playbook.md](references/browser-playbook.md)
- [issue-ledger.md](references/issue-ledger.md)
- [repair-and-reuse.md](references/repair-and-reuse.md)
- [release-and-rollback.md](references/release-and-rollback.md)
- [automation-promotion.md](references/automation-promotion.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown reports with evidence summaries, command blocks, and optional code, test, or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sanitized evidence references and local ledger paths; secrets and raw personal data should not be stored.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
