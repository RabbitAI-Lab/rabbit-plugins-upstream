## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use ShieldCortex to provide AI agents with persistent memory and to review or filter memory and tool content for prompt injection, credential leaks, and poisoning. Enforcement capabilities vary by agent host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OpenClaw hook's automatic startup self-heal can remove specified stale hook directories and copy hook files into the active hook path.

Mitigation: Review the documented startup behavior and affected local paths before enabling the hook.

Risk: When local binaries are unavailable, the hook may use npx to resolve packages that are not pinned in the skill instructions.

Mitigation: Inspect and install the required packages from trusted sources in advance, and review package resolution before enabling the hook.

Risk: The security scan had partial coverage, so its findings do not establish the complete behavior of the release.

Mitigation: Review the complete package and its referenced behavior before installation.

## Reference(s):

- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Security findings, Guidance]

**Output Format:** [Text and Markdown responses with memory context, security findings, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content depends on the user's memory, configuration, and enabled integrations]

## Skill Version(s):

5.19.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
