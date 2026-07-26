## Description: <br>
Applies an anti-sycophancy checklist to help an agent prioritize validity, evidence, and clear conclusions over agreeable but unverified responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill when they want an agent to challenge weak assumptions, avoid courtesy agreement, apply structured reasoning checks, and state conclusions based on evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate broadly during general analysis or debate and make the agent more direct. <br>
Mitigation: Use it where assumption-checking and evidence-based challenge are desired, and review final outputs for audience and tone fit. <br>
Risk: The artifact references a separate Night Market or Claude Code plugin experience that is not included in this release. <br>
Mitigation: Review any separately installed plugin, agent, hook, or command before relying on those components. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-rigorous-reasoning) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Priority signals](artifact/modules/priority-signals.md) <br>
- [Conflict analysis protocol](artifact/modules/conflict-analysis.md) <br>
- [Debate methodology](artifact/modules/debate-methodology.md) <br>
- [Correction protocol](artifact/modules/correction-protocol.md) <br>
- [Incremental reasoning](artifact/modules/incremental-reasoning.md) <br>
- [Pattern completion protocol](artifact/modules/pattern-completion.md) <br>
- [Engagement principles](artifact/modules/engagement-principles.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain-text reasoning guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only; no code execution, data access, persistence, or hidden actions are included in the artifact.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
