## Description: <br>
Agent Guild is a local-first protocol that lets joined AI agents share user identity, rules, current focus, logs, and handoff messages through plaintext Markdown and JSON under ~/.agent-guild/. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dqsjqian](https://clawhub.ai/user/dqsjqian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and power users who work with multiple local AI agents use this skill to give those agents a shared, local source of truth for user identity, rules, project focus, daily logs, and cross-agent handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores shared identity, rules, logs, handoffs, and registry state as plaintext local files. <br>
Mitigation: Use it only when plaintext cross-agent sharing is intended, and avoid storing secrets or sensitive personal data in ~/.agent-guild/ without a separate protection and cleanup plan. <br>
Risk: The documented install path includes executable setup steps that may be run directly from a remote script. <br>
Mitigation: Download a pinned release or installer script first, inspect it, and verify integrity before execution. <br>
Risk: Onboarding can create persistent files, symlinks, copies, registry entries, and shared cross-agent state. <br>
Mitigation: Require explicit approval before symlink, copy, delete, registry, or persistent write actions, and prefer atomic audited writes through the ac CLI. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/agent-guild) <br>
- [Agent Guild specification](https://github.com/dqsjqian/agent-guild/blob/main/docs/SPEC.md) <br>
- [Agent Guild onboarding guide](https://github.com/dqsjqian/agent-guild/blob/main/docs/ONBOARDING.md) <br>
- [Agent Guild runtime skill](https://github.com/dqsjqian/agent-guild/blob/main/SKILL.md) <br>
- [Agent Guild conventions](https://github.com/dqsjqian/agent-guild/blob/main/docs/CONVENTIONS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets, JSON state conventions, and local file path conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing instructions for reading and updating local shared files; persistent writes are expected to use the bundled ac CLI when available.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata; artifact frontmatter reports 3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
