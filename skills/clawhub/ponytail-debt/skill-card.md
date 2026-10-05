## Description:

Collects ponytail: shortcut comments from a repository into a technical-debt ledger with limits, upgrade triggers, and missing-trigger flags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to find marked shortcuts in a repository, record their limits and upgrade triggers, and flag debt without a trigger for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan reads repository source files, which may contain sensitive information.

Mitigation: Run it only against repositories the agent is authorized to read and review the ledger before sharing it.

Risk: Saving the ledger creates a repository file.

Mitigation: Request file output only when you intend to persist the ledger; otherwise use the read-only report.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-debt)
- [Project homepage listed in skill metadata](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text ledger grouped by file; optional Markdown file on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes file and line, shortcut description, limit, upgrade trigger, no-trigger flags, and a summary count; reports a clean ledger when no markers are found.]

## Skill Version(s):

4.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
