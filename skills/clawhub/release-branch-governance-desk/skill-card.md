## Description:

Selects a source branch for a release and assesses its release-branch policy status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release managers and developers use the skill to derive a source branch from a release request, assess it against the bundled branch-policy data, and record the local assessment when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream operation creates a local SQLite receipt in the chosen output directory.

Mitigation: Use a dedicated writable output directory and avoid sensitive shared locations.

Risk: A local assessment artifact could be mistaken for a completed external business action.

Mitigation: Treat it as a local record, not confirmation of an external action.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wxt-ai/skills/release-branch-governance-desk)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [JSON branch selection or policy assessment, with an optional local effect receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream assessment writes a local SQLite receipt only when an output directory is supplied.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
