## Description:

Reviews diffs for unnecessary complexity and suggests what to remove or replace in concise, numbered findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review code diffs for over-engineering and identify deletions, standard-library replacements, and simpler existing patterns without applying changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complexity-only review may overlook correctness, security, or performance issues.

Mitigation: Run a separate review for correctness, security, and performance before accepting changes.

Risk: Conversational text such as 'normal mode' may change or fail to change the intended review style.

Mitigation: Use explicit host controls to activate or stop the skill when precise control matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-review)
- [Skill homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Numbered, one-line findings with locations and suggested cuts or replacements, followed by a net line-reduction estimate; or a short no-findings verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review suggestions only; does not edit code.]

## Skill Version(s):

4.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
