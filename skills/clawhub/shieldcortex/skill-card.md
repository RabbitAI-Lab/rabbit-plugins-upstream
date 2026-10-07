## Description:

Provides persistent agent memory and security scanning for prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to recall information across sessions, organize memories, and scan agent content for security threats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic memory capture may persist sensitive conversation content.

Mitigation: Review saved memories and disable auto-memory on sensitive projects.

Risk: Bootstrap self-heal can modify agent hook locations without a prompt.

Mitigation: Disable self-heal when automatic hook changes are not desired.

Risk: Fallback execution may fetch and run a package from the npm registry.

Mitigation: Preinstall a trusted ShieldCortex binary or configure binaryPath.

Risk: Enabling Cloud sync can transmit stored memory data.

Mitigation: Keep Cloud sync off unless sharing memories is intended.

## Reference(s):

- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recalled memories and security scan findings.]

## Skill Version(s):

5.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
