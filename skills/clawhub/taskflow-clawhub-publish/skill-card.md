## Description:

Orchestrate a TaskFlow-managed ingestion job that validates, packages, and publishes an OpenClaw skill folder to the ClawHub registry, then verifies the published artifact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill to move an agent skill folder through a durable validate, publish, and verify workflow before it lands in the ClawHub registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publish step writes to the ClawHub registry and is explicitly irreversible.

Mitigation: Run the dry-run validation first and review the skill folder, slug, version, name, and changelog before allowing the publish step.

Risk: Incorrect user-supplied publish arguments could publish the wrong skill metadata or version.

Mitigation: Persist and review the selected publish arguments in TaskFlow state before executing the real publish command, then verify the resulting artifact by slug.

## Reference(s):

- [TaskFlow orchestration example](artifact/references/flow.ts)
- [ClawHub publish command example](artifact/references/publish.sh)
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/taskflow-clawhub-publish)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and TypeScript/Bash reference files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a TaskFlow flow plan, ClawHub publish commands, persisted state fields, and verification steps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
