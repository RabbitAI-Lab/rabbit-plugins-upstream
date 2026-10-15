## Description:

Provides persistent agent memory with semantic recall, knowledge graphs and security checks for prompt injection, credential leaks and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and retrieve agent knowledge while scanning memories and agent configuration for security threats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic memory capture may retain sensitive session content.

Mitigation: Review what auto-memory captures and disable extraction for sensitive workflows.

Risk: Hooks and updates can run automatically; the fallback npx path can execute an unpinned package.

Mitigation: Review hook, self-heal and update settings; prefer a pinned local installation or configured binaryPath.

Risk: Local scans can read agent configs and .env files, while optional cloud sync and webhooks can transmit selected data.

Mitigation: Review file access, synced content and webhook destinations before enabling these features.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ClawHub skill listing](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Security analysis]

**Output Format:** [Markdown with inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and scan results depend on the configured integration.]

## Skill Version(s):

5.10.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
