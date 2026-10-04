## Description:

Collects marked shortcut comments from a repository into a one-shot technical-debt ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to find marked shortcuts in a repository and identify debt entries missing a trigger to revisit them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saving a ledger creates a file in the repository.

Mitigation: Keep scans read-only by default; ask before writing a ledger file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dietrichgebert/skills/ponytail-debt)
- [Skill homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [File-grouped debt ledger with locations, ceilings, upgrade triggers, and a summary count]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marks entries without a trigger; reads files by default and writes a ledger only when asked.]

## Skill Version(s):

4.10.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
