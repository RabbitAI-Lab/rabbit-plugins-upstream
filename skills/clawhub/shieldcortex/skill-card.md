## Description:

Adds persistent agent memory, semantic recall, knowledge graphs, and security checks for prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and retrieve agent context, scan agent environments for security threats, and configure memory and protective integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks can self-heal and change hook files at gateway startup.

Mitigation: Review installed hooks and disable self-heal if automatic changes are unwanted.

Risk: Agent configuration, optional .env files, and conversation transcripts may contain sensitive data retained in local memory.

Mitigation: Review auto-memory and keyword-trigger settings and limit access to locally retained data.

Risk: Fallback package execution may download ShieldCortex at runtime.

Mitigation: Install ShieldCortex locally rather than relying on the npx fallback.

Risk: Enabling Cloud sync can send selected memory data outside the local environment.

Mitigation: Leave Cloud sync off unless you explicitly want memory data synced.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and scan findings depend on local agent data and enabled integrations.]

## Skill Version(s):

5.2.0 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
