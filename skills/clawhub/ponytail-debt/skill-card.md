## Description:

Collects marked shortcut comments into a technical-debt ledger and flags entries without a trigger to revisit them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to find marked shortcuts in a repository, group them into a debt ledger, and spot deferrals with no upgrade trigger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger entries may be incomplete or misleading when comments do not explain the deferral or its upgrade trigger.

Mitigation: Review the generated ledger against the source comments before acting on it.

Risk: The broad phrase 'normal mode' may unintentionally stop the skill.

Mitigation: Use the explicit 'stop ponytail-debt' command when intentionally leaving the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-debt)
- [Skill homepage (listed in metadata)](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Ledger rows grouped by file, optionally saved as a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ends with marker and no-trigger counts; reports a clean ledger when no markers are found.]

## Skill Version(s):

5.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
