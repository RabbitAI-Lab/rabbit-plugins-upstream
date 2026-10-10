## Description:

Inventories office-agent skills, estimates their context cost, identifies duplicates, and recommends which skills to keep, review, or consider disabling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Office-agent users and administrators use this skill to audit installed skills, assess usage and dependencies, and review candidates for disabling before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory may read local skill directories, usage logs, and automation or plugin configuration.

Mitigation: Run it only where access to those local files is appropriate and review the selected paths.

Risk: Applying a proposed disablement changes persistent skill settings and can affect agent behavior.

Mitigation: Review the dry-run and backup path, then use --overrides --apply --yes only after explicit confirmation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/skill-inventory)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration guidance]

**Output Format:** [Human-readable inventory report or English-keyed JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports skill usage, estimated context cost, dependencies, and conservative disablement candidates; settings changes require explicit consent.]

## Skill Version(s):

1.5.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
