## Description:

A minimal, reproducible runbook for chaining a business-process tool (TaskFlow-style workspace orchestration) with the ClawHub CLI to turn processed digital content into a discoverable, installable resource-center entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to package processed workspace content as a minimal ClawHub skill, preview publication with a dry run, publish it, and verify that it is searchable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can make the resource-center entry visible and installable.

Mitigation: Review the slug, account identity, and package contents, then run the dry-run publish step before publishing.

Risk: Publishing under the wrong account or a colliding slug can create an incorrect resource entry.

Mitigation: Run clawhub whoami and confirm slug availability before publishing.

Risk: Low-quality source description content can reduce discoverability after ingestion.

Mitigation: Review DESCRIPTION.md before publication so the packaged summary accurately describes the resource.

## Reference(s):

- [ClawHub Ingest Runbook release page](https://clawhub.ai/terrycarter1985/skills/hub-ingest-runbook)
- [Publisher profile: terrycarter1985](https://clawhub.ai/user/terrycarter1985)
- [DESCRIPTION.md](references/DESCRIPTION.md)
- [workflow-handoff.md](workflow-handoff.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown runbook with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the clawhub CLI and an authenticated ClawHub identity for publishing steps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
