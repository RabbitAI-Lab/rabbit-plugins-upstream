## Description:

Regression-test Open WebUI tools, adapters, streaming, reconnects, provider limits, and TTS through the real browser path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to verify Open WebUI regressions through the real logged-in browser path, including tool calls, adapters, streaming, reconnect behavior, provider limits, and TTS. It helps map failures to the responsible request-chain layer while preserving database and user state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Testing may involve logged-in browser sessions, service logs, provider calls, and database checks.

Mitigation: Run tests only when real-path validation is intended, limit activity to disposable chats, and use only user-approved service restarts.

Risk: Regression work can accidentally disturb live Open WebUI account data or database state.

Mitigation: Preserve the existing database and unrelated user state, remove only disposable test chats, and confirm database integrity after material changes.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/pinguy/Skills/tree/main/skills/openwebui-regression-test)
- [ClawHub skill page](https://clawhub.ai/pinguy/skills/openwebui-regression-test)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with checklists and command or code snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on user-visible browser-path validation and concise reporting of tested and untested boundaries.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
