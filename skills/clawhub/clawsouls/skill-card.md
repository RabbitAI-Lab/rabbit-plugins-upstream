## Description:

Helps agents manage personas across supported workspaces, including installing and switching Souls, publishing personas, and optionally syncing encrypted memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent users use this skill to find, install, activate, restore, and publish AI personas in OpenClaw, Hermes Agent, ZeroClaw, and compatible workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Switching personas persistently changes agent identity files.

Mitigation: Confirm the exact files that will change before switching and keep a restorable backup.

Risk: Publishing a Soul can expose private prompts or secrets.

Mitigation: Review every file in the soul directory before authorizing publication.

Risk: Explicit sync and swarm commands transfer agent memory to a Git remote.

Mitigation: Confirm the destination and contents before syncing, and run these commands only on explicit request.

Risk: The bundled wrapper can execute a currently resolved, unpinned npm package.

Mitigation: Avoid the wrapper unless current npm package resolution is trusted; prefer reviewed, pinned CLI invocations.

## Reference(s):

- [Clawsouls Skill on ClawHub](https://clawhub.ai/tomleelive/skills/clawsouls)
- [ClawSouls registry](https://clawsouls.ai)
- [Soul-Driven Interaction Design](https://doi.org/10.5281/zenodo.18772585)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persona actions may modify workspace files or contact external services.]

## Skill Version(s):

0.6.7 (source: SKILL.md frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
