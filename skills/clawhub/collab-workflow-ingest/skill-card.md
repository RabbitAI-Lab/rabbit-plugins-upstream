## Description:

Collab Workflow Ingest guides an agent through clarifying vague business process requirements, packaging the structured handoff as a ClawHub skill asset, and publishing it to the ClawHub resource center.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workflow authors use this skill to turn unclear business process requests into structured steps, then package and publish the resulting workflow documentation as a searchable ClawHub skill asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can produce a weak or unusable asset if requirement clarification is skipped or rushed.

Mitigation: Complete the staged workflow-structurer clarification and review the generated DESCRIPTION.md before packaging.

Risk: Published workflow documentation may include confidential business details.

Mitigation: Review and remove sensitive information before running the final ClawHub publish command.

Risk: A malformed package or duplicate slug can cause publishing to fail.

Mitigation: Run the dry-run publish step first and confirm the slug is unique before final publication.

## Reference(s):

- [Workflow Handoff Description](references/DESCRIPTION.md)
- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/collab-workflow-ingest)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with bash command examples and file layout snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a structured workflow handoff and ClawHub skill packaging guidance when followed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
