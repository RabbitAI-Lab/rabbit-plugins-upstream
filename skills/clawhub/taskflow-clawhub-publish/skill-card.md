## Description:

Orchestrate a TaskFlow-managed ingestion job that validates, packages, and publishes an OpenClaw skill folder to the ClawHub registry, then verifies the published artifact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill to run an auditable, resumable workflow for validating, publishing, and verifying OpenClaw skills on ClawHub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The real publish step writes to the ClawHub registry and is described as irreversible.

Mitigation: Run the dry-run validation step first and manually confirm the target skill folder, slug, name, version, and changelog before publishing.

Risk: A completed publish may not match the intended release metadata.

Mitigation: Inspect the published skill and, when appropriate, install it into a temporary directory to confirm the installed metadata version.

## Reference(s):

- [TaskFlow orchestration shape](artifact/references/flow.ts)
- [Publish command sequence](artifact/references/publish.sh)
- [Published artifact verification commands](artifact/references/inspect.sh)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run validation, irreversible publish, and post-publish verification steps.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
