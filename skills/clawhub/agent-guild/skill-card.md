## Description:

Agent Guild is a local-first, plaintext protocol and runtime skill that lets multiple AI agents on the same machine share identity, rules, memory, current focus, handoff messages, logs, and learning ledgers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users of multiple local AI agents use this skill to give agents a shared filesystem-backed memory and coordination space. Agents can onboard themselves, read shared user context, exchange handoffs, append work logs, and maintain reusable learnings without a hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates shared persistent plaintext memory on the local machine, which can expose sensitive user context if agents record secrets or if the directory is backed up or synced without care.

Mitigation: Install only when plaintext local memory is intended; do not record secrets, raw transcripts, tokens, keys, or cookies, and keep sensitive connector credentials outside normal skill data.

Risk: The skill gives agents authority to modify ~/.agent-guild/ and to link or copy the skill into agent-specific skill directories.

Mitigation: Review the onboarding flow first, keep adoption dry-run by default, and inspect planned changes before running adopt --apply.

Risk: Upgrade and installer flows can fetch remote release content, which adds supply-chain risk if run blindly.

Mitigation: Avoid blind pipe-to-shell installation, inspect the remote source or release package before applying updates, and run upgrade --apply only from a trusted source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Project homepage](https://github.com/dqsjqian/agent-guild)
- [Agent Guild specification](docs/SPEC.md)
- [Onboarding flow](docs/ONBOARDING.md)
- [Conventions](docs/CONVENTIONS.md)
- [Learning ledger](docs/LEARNINGS.md)
- [Machine-readable manifest](manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands, file paths, and CLI text output; runtime state is stored as local Markdown and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes persistent local files under ~/.agent-guild/ when agents follow the skill's onboarding and runtime commands.]

## Skill Version(s):

3.6.1 (source: SKILL.md frontmatter, manifest.json, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
