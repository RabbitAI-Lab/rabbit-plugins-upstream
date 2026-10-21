## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this agent skill to support AI-agent memory, semantic recall, and knowledge-graph use, while scanning and enforcing against prompt injection, credential leaks, and poisoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approval controls are ignored, and automatic repairs can erase customized hook files.

Mitigation: Keep the bundled realtime plugin disabled until approval handling is corrected; back up customized hooks and consider SHIELDCORTEX_SKIP_SELF_HEAL=1 before enabling the hook.

Risk: Automatically saved memories may need review.

Mitigation: Review automatically saved memories before relying on them.

## Reference(s):

- [ShieldCortex on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex on npm](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Security guidance]

**Output Format:** [Natural-language text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the agent's memory or security task.]

## Skill Version(s):

5.10.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
