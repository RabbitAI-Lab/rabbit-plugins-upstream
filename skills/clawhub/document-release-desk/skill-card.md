## Description:

Derive release selection rules and select document releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document release teams use this skill to define release selection guidance and choose eligible document versions within a requested major release line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unclear selection guidance could lead to choosing the wrong document release.

Mitigation: Provide the target major version and approval requirements, then review the selection result before using it for release decisions.

Risk: The skill output could be mistaken for a publishing or overwrite action.

Mitigation: Treat the output as a selection recommendation only; the evidence states it does not request publishing authority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/document-release-desk)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Concise text and structured selection result object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces selection_guidance and selection_result with selected_version, eligible_versions, and reason.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
