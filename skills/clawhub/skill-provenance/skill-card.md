## Description:

Version, validate, package, verify, recover, and hand off Agent Skill bundles across local folders, registries, platform uploads, and agent sessions. Use for MANIFEST.yaml, CHANGELOG.md, bundle hashes, stale evals, frontmatter portability, derived skill packages, or version identity that must survive filename changes and cross-platform movement. Do not use for ordinary Git version control that does not involve an Agent Skill bundle. Compatible with the agentskills.io open standard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snapsynapse](https://clawhub.ai/user/snapsynapse)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to keep Agent Skill bundles traceable across local folders, registries, platform uploads, and agent sessions. It helps verify file inventory and hashes, manage changelogs and bundle versions, prepare derived packages, and surface drift before handoff or deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary flags the fallback verification path because it may ask agents to run a shell script downloaded from a mutable website.

Mitigation: Before installation or invocation, decide whether the publisher and distribution channel are trusted; inspect any wrapper, prefer authenticated or pinned sources, and ask for proposed diffs before allowing writes.

Risk: Bootstrap and packaging workflows can modify bundle metadata, manifests, hashes, changelogs, or derived package files.

Mitigation: Name the target bundle directory explicitly, run validation first, and review proposed file changes before accepting mutations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snapsynapse/skills/skill-provenance)
- [Publisher profile](https://clawhub.ai/user/snapsynapse)
- [Assistant guide](https://skillprovenance.dev/.well-known/assistant-guide.txt)
- [Packaging and changelog reference](references/packaging-and-changelog.md)
- [Platform and trust reference](references/platforms-and-trust.md)
- [Standalone verification reference](references/standalone-verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML, JSON, and shell command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update bundle files such as MANIFEST.yaml, CHANGELOG.md, handoff notes, package manifests, and version metadata when the user authorizes mutations.]

## Skill Version(s):

6.3.0 (source: server release metadata and MANIFEST.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
