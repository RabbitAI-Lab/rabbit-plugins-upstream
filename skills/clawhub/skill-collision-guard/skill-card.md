## Description:

Check for overlapping, duplicate, shadowing, or contradictory coding-agent skills before installing a skill/plugin or when multiple skills may trigger; compare them and help remove or reversibly suppress one for the current session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[three-liu](https://clawhub.ai/user/three-liu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use this skill to scan installed and candidate skills for name shadowing, duplicate capabilities, policy conflicts, and behavioral interference before installation or invocation. It helps them compare conflicts and choose reversible session suppression when only one skill should apply temporarily.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory scans read installed SKILL.md files from configured agent skill roots, which may expose local instruction content to the current agent session.

Mitigation: Use the --agent option to scope scans to the current agent and review findings before acting on them.

Risk: Remote candidate checks may clone a repository for inspection.

Mitigation: Inspect only trusted candidate references; the skill uses a temporary directory and a default timeout for remote clone inspection.

Risk: Conflict recommendations can change which skill is followed during a session.

Mitigation: Prefer reversible session suppression and require an explicit user decision before permanently removing, renaming, or editing an installed skill.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON reports with recommended shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The check-install command exits with status 2 when installation needs a user decision.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
