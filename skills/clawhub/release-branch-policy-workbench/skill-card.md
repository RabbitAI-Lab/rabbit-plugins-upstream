## Description:

Assesses a release branch against bundled policy data and records the result locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release managers and developers use this skill to assess a named release branch against the bundled policy catalog and keep a local assessment record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a local SQLite record in the selected output directory.

Mitigation: Choose a dedicated writable output directory and review the record before sharing it.

Risk: The assessment uses bundled branch data, not live repository state.

Mitigation: Confirm branch status against the authoritative repository before release decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Files]

**Output Format:** [JSON assessment and local SQLite record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes branch status, version alignment, policy status, and a local artifact receipt.]

## Skill Version(s):

1.1.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
