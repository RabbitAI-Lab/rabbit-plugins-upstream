## Description:

Step-by-step runbook for pairing TaskFlow (business process orchestration) with ClawHub (skill registry ingestion) to publish a digital skill artifact to the ClawHub resource center.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill as a repeatable checklist for validating, publishing, and verifying a ClawHub skill release coordinated through TaskFlow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The non-dry-run publish command changes registry state.

Mitigation: Confirm the skill folder path, destination slug, version, changelog, and authenticated ClawHub account before running the publish command without --dry-run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/taskflow-clawhub-upload-runbook)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Procedural runbook output; publishing commands should be reviewed before non-dry-run execution.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
