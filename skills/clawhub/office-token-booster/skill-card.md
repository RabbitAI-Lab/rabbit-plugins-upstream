## Description:

A local office assistant that drafts work products, analyzes AI token usage, and tracks estimated time and token savings in a ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Office workers use this skill to draft weekly reports, meeting notes, document summaries, data analyses, and presentation outlines. They can also review local token usage and estimate productivity gains from a task ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected office files and can write reports and ledger files.

Mitigation: Review file paths and outputs before running commands; keep network access disabled as declared.

Risk: Confirming a ledger update or importing local host usage traces can add sensitive or inaccurate records.

Mitigation: Preview proposed changes, verify the input and baseline estimates, and confirm ledger writeback only when intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/office-token-booster)
- [Quickstart](artifact/QUICKSTART.md)
- [Portability contract](artifact/docs/portability-contract.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML reports, JSON ledger entries, Guidance]

**Output Format:** [Conversational text and local Markdown, HTML, or JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Savings are estimates based on user-provided baselines; ledger updates require confirmation.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
