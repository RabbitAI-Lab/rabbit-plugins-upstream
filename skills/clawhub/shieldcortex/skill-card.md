## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using supported coding agents use ShieldCortex to maintain searchable memory and review prompt-injection, credential-leak, and poisoning risks. Enforcement depends on the host integration; some hosts provide a memory server without a bound tool gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because some referenced local paths could not be resolved; the supplied verdict is suspicious with medium confidence.

Mitigation: Treat the verdict as suspicious before installing. Review the unresolved files and package references, and do not proceed when their contents cannot be verified.

Risk: The OpenClaw hook can use npx to resolve packages when local binaries are unavailable, which can execute packages fetched at runtime.

Mitigation: Inspect and preinstall the required packages at fixed versions, then confirm the hook can find those local binaries before enabling it.

Risk: At gateway bootstrap, the hook can copy files or remove two named legacy hook directories without prompting or taking a backup.

Mitigation: Review those paths and preserve any needed files before enabling the hook; verify the expected hook location after setup.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)
- [ShieldCortex issue tracker](https://github.com/Drakon-Systems-Ltd/ShieldCortex/issues)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Security analysis]

**Output Format:** [Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Host-dependent enforcement; the skill describes a package and integrations rather than shipping executable code.]

## Skill Version(s):

5.20.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
