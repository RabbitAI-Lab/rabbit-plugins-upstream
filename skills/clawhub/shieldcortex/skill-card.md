## Description:

ShieldCortex gives AI agents persistent semantic memory and scans memory and agent instructions for prompt injection, credential leaks, and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to store and recall context across sessions, inspect agent instructions and memory for threats, and configure security checks for supported hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic memory capture can retain sensitive conversation content across sessions.

Mitigation: Review auto-memory and proactive-recall settings, and disable auto-extraction for sensitive work.

Risk: Automatic hook repair can delete or copy hook files without a prompt, including during legacy migration.

Mitigation: Disable self-heal if unwanted, and back up or inspect legacy ~/.clawdbot hook directories before first OpenClaw startup.

Risk: The OpenClaw npx fallback can download and run the package when no local install is available.

Mitigation: Prefer a pinned local ShieldCortex install over the npx fallback.

Risk: Opt-in Cloud sync can upload stored memory content.

Mitigation: Keep Cloud sync off unless you intend to upload memory content.

## Reference(s):

- [ShieldCortex on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with command examples and memory or scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and scan results depend on local configuration and host integration.]

## Skill Version(s):

5.10.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
