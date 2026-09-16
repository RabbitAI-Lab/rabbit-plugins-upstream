## Description:

OpenClaw Context Budget helps an agent inspect enabled OpenClaw model context-window settings, fetch official vendor context-window values, propose a 60% window target, and patch only the contextWindow field after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to audit active model context-window settings and apply scoped configuration updates when the current window differs from official vendor specifications. The workflow is read-only until the user confirms a proposed change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing contextWindow values can affect OpenClaw runtime behavior.

Mitigation: The skill presents the proposed old-to-new change and waits for explicit user confirmation before patching only contextWindow fields.

Risk: Unofficial or unresolved vendor context-window sources could lead to incorrect recommendations.

Mitigation: The workflow prefers official vendor sources and tells users not to confirm changes based on unofficial or unresolved sources.

Risk: Configuration reads may return more data than the skill needs.

Mitigation: The release scope is limited to window-related fields, and credential-bearing or unrelated configuration sections are ignored and not echoed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-context-budget)
- [README.en.md](README.en.md)
- [Design Document](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown decision cards and concise text responses, with optional shell commands for reload guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces proposed OpenClaw contextWindow changes only; the skill itself generates no files, scripts, or scheduled jobs.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
