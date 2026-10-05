## Description:

Plans an archive-style CSV path from a document kind and account reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge-base publishers use this skill to derive a consistent archive CSV path from a document kind and account reference before placing a record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The returned archive CSV path may be mistaken for a knowledge-base article location.

Mitigation: Confirm that an archive-style CSV path is the intended destination before using it in downstream systems.

## Reference(s):

- [Knowledge Placement Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-note-path-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON containing a path string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an archives/*.csv path; does not create a file.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
