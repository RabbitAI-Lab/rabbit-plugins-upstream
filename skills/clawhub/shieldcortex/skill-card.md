## Description:

ShieldCortex provides persistent agent memory with semantic recall, a knowledge graph, and safeguards against prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and retrieve agent knowledge across sessions while screening memory and agent inputs for security threats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OpenClaw hook can install persistent files automatically during startup.

Mitigation: Review the hook before installation and disable or explicitly approve self-heal behavior.

Risk: A missing local installation may trigger an npx download and execution.

Mitigation: Use a pinned local ShieldCortex installation instead of the npx fallback.

Risk: Automatic memory capture may retain sensitive session content or secrets.

Mitigation: Review captured memories and disable auto-memory for sensitive work.

Risk: Enabling cloud sync can upload stored memory content.

Mitigation: Leave cloud sync off unless its documented uploads are acceptable.

## Reference(s):

- [ShieldCortex on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown with commands and memory-recall results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface locally retained memories and security scan findings.]

## Skill Version(s):

5.2.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
