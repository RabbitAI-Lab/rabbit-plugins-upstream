## Description:

Skill Provenance provides portable version identity, integrity verification, changelogs, and drift detection for Agent Skill bundles across repositories, registries, platforms, and agent sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this agent skill to version, validate, package, recover, and hand off multi-file Agent Skill bundles across local folders, registries, platform uploads, and agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose shell commands for verification or packaging.

Mitigation: Review commands before execution, especially external verification or package helper commands.

Risk: Passing hash validation confirms file consistency but does not prove publisher identity or overall safety.

Mitigation: Treat manifest and hash checks as integrity evidence, and use server-resolved publisher and provenance fields for ownership context.

Risk: The skill can manage provenance files for skill bundles, including manifests, changelogs, and handoff material.

Mitigation: Inspect proposed file changes before deployment, publication, or handoff.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/snapsynapse/skills/skill-provenance)
- [Packaging and changelog reference](references/packaging-and-changelog.md)
- [Platform, ecosystem, and trust reference](references/platforms-and-trust.md)
- [Standalone verification and bootstrap](references/standalone-verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and file-oriented configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include manifest and changelog updates, package commands, verification summaries, and handoff notes.]

## Skill Version(s):

6.2.0 (source: evidence.release.version and MANIFEST.yaml bundle_version, released 2026-08-28)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
