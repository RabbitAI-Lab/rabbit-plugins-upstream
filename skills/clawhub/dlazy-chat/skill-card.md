## Description:

Connects users to a project-scoped dLazy sandbox agent for multi-turn conversations and skill-based tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can start or resume project-based conversations with a hosted sandbox agent, select available skills, and optionally attach reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat triggers may route ordinary conversations to an authenticated remote dLazy service.

Mitigation: Review the skill before installation and invoke it only when intending to use dLazy, especially if a local-only workflow is preferred.

Risk: Prompts and attached files can leave the device; attached files are uploaded to dLazy storage.

Mitigation: Do not attach secrets or sensitive files unless you explicitly intend to upload them.

Risk: Logging in persists an API key in local CLI configuration.

Mitigation: Use a per-invocation API key if less local credential persistence is desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streamed conversational text, potentially containing Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped responses can continue across turns.]

## Skill Version(s):

1.2.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
