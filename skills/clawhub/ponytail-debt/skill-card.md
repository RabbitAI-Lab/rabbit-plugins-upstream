## Description:

Collects marked shortcut comments into a one-shot debt ledger so deferred work stays visible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to find marked shortcuts in a repository and review their stated limits and upgrade triggers in a grouped debt ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans repository comments, which may include material the user does not want reviewed.

Mitigation: Run it only on repositories whose text the user is comfortable having scanned.

Risk: Saving a ledger changes the repository.

Mitigation: Keep the report read-only unless the user explicitly asks to save it.

Risk: Shortcut markers without upgrade triggers can linger unresolved.

Mitigation: Tag those entries as no-trigger and review them for a concrete revisit condition.

## Reference(s):

- [Project homepage (ClawHub metadata)](https://github.com/DietrichGebert/ponytail)
- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-debt)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown ledger grouped by file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One row per marker with file, line, simplification, ceiling, and upgrade trigger; tags missing triggers and ends with totals or a clean-ledger message. Writes a file only when asked.]

## Skill Version(s):

5.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
