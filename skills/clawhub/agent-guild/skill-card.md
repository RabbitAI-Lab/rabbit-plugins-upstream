## Description:

Agent Guild provides local-first cross-agent shared memory so multiple AI agents on one machine can share identity, rules, focus, logs, and handoff messages through plaintext Markdown and JSON files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use Agent Guild to onboard multiple local agents into a shared filesystem-based memory and coordination protocol. Joined agents can read and update persistent identity, rules, project focus, daily logs, and handoff messages across those agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a plaintext local memory and tool-sharing bus that can expose user identity, routines, rules, logs, and handoff messages to joined agents on the same machine.

Mitigation: Install only when this sharing model is intended, keep secrets out of Agent Guild state, and review shared memory before syncing or backing up the directory.

Risk: The skill includes flows for installing, upgrading, adopting assets, and sharing persistent tooling across agents.

Mitigation: Review installer and upgrade sources before running remote commands, avoid unverified auto-upgrades, and require explicit confirmation before `adopt --apply` or new shared tool installs.

Risk: Cross-agent memory writes can persist incorrect or overly broad user context for future agents.

Mitigation: Require confirmation before writing cross-agent memory and prefer scoped, auditable updates through the provided CLI or in-place edits.

## Reference(s):

- [Agent Guild Repository Homepage](https://github.com/dqsjqian/agent-guild)
- [Agent Guild ClawHub Skill Page](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Agent Guild Specification](artifact/docs/SPEC.md)
- [Agent Guild Onboarding Guide](artifact/docs/ONBOARDING.md)
- [Agent Guild Conventions](artifact/docs/CONVENTIONS.md)
- [Agent Guild Manifest](artifact/manifest.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, filesystem paths, and JSON or Markdown state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plaintext local state under the Agent Guild directory when its commands or file-edit instructions are applied.]

## Skill Version(s):

3.4.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
