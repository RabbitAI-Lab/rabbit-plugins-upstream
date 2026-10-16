## Description:

Helps users review multi-asset portfolios, analyze investments with an AI committee, and record position changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors and their agents use this skill to monitor holdings and prices, review AI-generated investment verdicts, and record portfolio changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Coordinator/Hermes committee workflow can execute shell code derived from untrusted news-influenced model output.

Mitigation: Avoid the Coordinator/Hermes path until transcript persistence is fixed; use the Direct committee path instead.

Risk: Development mode in an untrusted directory and exposed API keys can compromise local investment data or credentials.

Mitigation: Do not enable OPENINVEST_DEV_MODE in untrusted directories; keep .env secrets local.

Risk: Portfolio ledger changes can record unintended transactions.

Mitigation: Confirm each ledger-changing action with the user before recording it.

## Reference(s):

- [openInvest on ClawHub](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Committee workflows](artifact/references/two-paths.md)
- [Tool reference](artifact/references/tools.md)
- [Project architecture wiki (documentation, not verified release provenance)](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Shell commands]

**Output Format:** [Markdown responses and reports; structured JSON verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can record portfolio transactions and committee decisions when requested.]

## Skill Version(s):

0.25.0 (source: release metadata, skill frontmatter and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
