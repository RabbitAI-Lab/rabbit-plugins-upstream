## Description:

Provides AI agents with persistent semantic memory, knowledge-graph recall, and scans for prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and recall agent knowledge, scan content for security threats, and configure memory and security integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent lifecycle hooks can access sensitive local agent data.

Mitigation: Review installed hooks and disable auto-memory if automatic capture is not wanted.

Risk: Cloud sync can transmit stored memory content when enabled.

Mitigation: Keep cloud sync off unless needed and review which memories are eligible to sync.

Risk: Self-heal and the npx fallback can install or fetch components without a separate manual install step.

Mitigation: Review self-heal settings, disable self-heal for manual control, and install the package locally to avoid the fallback download.

## Reference(s):

- [ShieldCortex on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub profile (release metadata)](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide installation of local memory and security integrations.]

## Skill Version(s):

5.10.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
