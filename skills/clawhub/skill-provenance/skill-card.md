## Description:

Version, validate, package, verify, recover, and hand off Agent Skill bundles across local folders, registries, platform uploads, and agent sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to keep multi-file Agent Skill bundles traceable across local editing, registry publication, platform uploads, and agent sessions. It supports manifest-based inventory, changelog discipline, hash checks, derived packages, handoffs, and drift review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running bootstrap, validation update, or packaging workflows in the wrong directory could read, hash, update, or package unintended skill bundle files.

Mitigation: Confirm the intended bundle directory before running those workflows and review manifest, changelog, handoff, and derived package changes before publishing or reinstalling.

Risk: Manifest hashes, changelogs, and deployment notes can be mistaken for proof that a skill is safe or trustworthy.

Mitigation: Treat them as integrity and drift evidence only; review and scan the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snapsynapse/skills/skill-provenance)
- [Skill Provenance README](README.md)
- [Packaging and changelog reference](references/packaging-and-changelog.md)
- [Platform, ecosystem, and trust reference](references/platforms-and-trust.md)
- [GuideCheck assistant guide](https://skillprovenance.dev/.well-known/assistant-guide.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or update bundle files such as MANIFEST.yaml, CHANGELOG.md, handoff notes, and derived package inventories when the user asks for bundle maintenance.]

## Skill Version(s):

6.1.0 (source: server release evidence and MANIFEST.yaml bundle_version, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
