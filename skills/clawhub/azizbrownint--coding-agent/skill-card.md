## Description:

Delegate coding work to Codex, Claude Code, or OpenCode as background workers; not simple edits or read-only code lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to delegate background feature builds, PR reviews, large refactors, and issue-to-PR development to Codex, Claude Code, or OpenCode workers while preserving notification and reporting expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background coding agents may run unattended with broad repository execution authority.

Mitigation: Use trusted isolated repositories, minimize exposed environment secrets, and monitor worker sessions before accepting changes.

Risk: The Claude Code launch path disables permission prompts.

Mitigation: Use the Claude Code path only when disabled permission prompts are intentionally accepted; prefer sandboxed workdirs and alternatives when appropriate.

Risk: Completion reporting can fail when notification routing is missing or untrusted.

Mitigation: Capture a trustworthy notification route before spawning workers and require exactly one completion or failure message.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/azizbrownint/skills/coding-agent)
- [Claude Code CLI npm Package](https://www.npmjs.com/package/@anthropic-ai/claude-code)
- [Codex CLI npm Package](https://www.npmjs.com/package/@openai/codex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with text and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires one of claude, codex, or opencode and a configured notification route.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
