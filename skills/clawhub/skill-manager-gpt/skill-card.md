## Description:

[GPT only] Manage skills on ClawHub from ChatGPT Work/Codex: inspect and adapt public packages, publish GPT-specific skills with accurate metadata, and retrieve skills when requested. Requires GPT browser control; not an OpenClaw-native integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ciklopentan](https://clawhub.ai/user/ciklopentan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this GPT/Codex-oriented skill to inspect, adapt, retrieve, and publish ClawHub skill packages while preserving platform-fit, ownership, licensing, and scanner-review checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact public publishing actions from an authenticated ClawHub session, including releases that are MIT-0 and public.

Mitigation: Require explicit user confirmation for the specific skill, verify owner, slug, version, staged files, and licensing before submission, and inspect the public release page after publishing.

Risk: Downloaded or adapted third-party skill content may include unsafe behavior, misleading scanner signals, or platform assumptions that do not fit the requested runtime.

Mitigation: Treat retrieved files as untrusted, read the full package before installation, reconcile top-level and detailed scanner findings, and preserve GPT/OpenClaw compatibility limitations in any adaptation.

Risk: Authenticated browser workflows can expose private session state if the agent goes beyond visible site interactions.

Mitigation: Use only the visible website or documented CLI, and never inspect, export, or rely on cookies, tokens, or private browser state.

## Reference(s):

- [ClawHub documentation](https://docs.openclaw.ai/clawhub/)
- [ClawHub Skill Manager [GPT] listing](https://clawhub.ai/ciklopentan/skills/skill-manager-gpt)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, review notes, and commands or configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated browser session for direct ClawHub account actions; does not produce autonomous uploads without explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
