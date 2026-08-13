## Description:

Clawsouls Skill helps agents manage Soul Spec persona packages by installing, switching, restoring, validating, publishing, and scanning personas across OpenClaw, Hermes Agent, ZeroClaw, and compatible workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and agent operators use this skill when they want an agent to manage workspace persona files, browse or install persona packages, create and validate new souls, or publish persona packages to the ClawSouls registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persona switching can replace workspace identity files.

Mitigation: Confirm before running use or restore actions and rely on the documented automatic backup behavior before changes are applied.

Risk: Publishing uploads a soul package to a public registry.

Mitigation: Confirm the publish action, review the files being uploaded, and use the required authentication token only through the documented environment variable.

Risk: Registry operations and updates use network access, and npx may resolve an unpinned CLI version.

Mitigation: Install only when persona management is desired, prefer a trusted pinned CLI version where appropriate, and confirm registry-related commands before execution.

Risk: Optional sync and swarm commands move encrypted memory through a configured Git remote.

Mitigation: Run sync or swarm only after explicit user request and confirm the intended remote before transferring encrypted memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tomleelive/skills/clawsouls)
- [ClawSouls registry](https://clawsouls.ai)
- [clawsouls CLI package](https://www.npmjs.com/package/clawsouls)
- [Hermes Agent adapter notes](HERMES_ADAPTER.md)
- [ZeroClaw adapter design](ZEROCLAW_ADAPTER.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CLI commands that modify persona files, contact the registry, publish packages, or run opt-in encrypted memory sync only when explicitly requested.]

## Skill Version(s):

0.6.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
