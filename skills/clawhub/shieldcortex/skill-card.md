## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex to give supported AI agent environments persistent memory and scan or enforce protections against prompt injection, credential exposure, and poisoned content. Enforcement depends on the integration; some environments provide an MCP memory server without a bound tool gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports unattended retrieval of unpinned packages, and its review did not analyze executable package files.

Mitigation: Review the npm package and resolved dependencies before installation; use pinned versions and avoid automatic package resolution where practical.

Risk: The documented OpenClaw bootstrap self-heal can copy hook files and delete two legacy hook directories without a backup.

Mitigation: Inspect the affected hook directories first; disable self-heal with `shieldcortex config --self-heal false` or `SHIELDCORTEX_SKIP_SELF_HEAL=1` if those automatic changes are not acceptable.

Risk: The skill documents outbound requests that can occur without an explicit request, including an embedding-model download and package-version lookups.

Mitigation: Review the listed network behavior and disable embedding downloads or dashboard update checks when appropriate; these switches do not disable every network path.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex release on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [Repository link listed in the skill file (import provenance unavailable)](https://github.com/Drakon-Systems-Ltd/ShieldCortex)
- [Dependency audit waivers listed in the skill file](https://github.com/Drakon-Systems-Ltd/ShieldCortex/blob/main/docs/security/audit-waivers.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes memory and security workflows; the skill file contains no executable code.]

## Skill Version(s):

5.21.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
