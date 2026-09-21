## Description:

Agent Guild lets multiple local AI agents share plaintext Markdown and JSON identity, rules, memory, handoffs, logs, and skill state through a local filesystem protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use Agent Guild to let multiple local AI agents share durable user context, rules, current focus, inbox messages, daily logs, and cross-agent learnings without a hosted memory service. It is intended for local-first workflows where agents can read files and optionally run the bundled Python CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill centralizes plaintext memory, rules, logs, handoffs, and shared skills under ~/.agent-guild/.

Mitigation: Use it only for workflows where local plaintext sharing across agents is intentional, and avoid storing secrets or credentials in shared memory.

Risk: Shared rules and a common skill bus can change behavior across multiple agents at once.

Mitigation: Review shared rules, adopted skills, and installation changes before enabling them for additional agents.

Risk: Self-update and install paths can replace skill files from a remote release source.

Mitigation: Keep auto-upgrade mode off unless the release source is trusted, and review upgrade actions before using apply modes.

Risk: Adopt, link-root, and portability commands can move files or create links.

Mitigation: Use dry-run output first and review what will be symlinked, adopted, or moved before running commands with --apply.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Project homepage](https://github.com/dqsjqian/agent-guild)
- [Agent Guild specification](https://github.com/dqsjqian/agent-guild/blob/main/docs/SPEC.md)
- [Onboarding guide](https://github.com/dqsjqian/agent-guild/blob/main/docs/ONBOARDING.md)
- [Security disclosure](https://github.com/dqsjqian/agent-guild/blob/main/docs/SECURITY.md)
- [Portability guide](https://github.com/dqsjqian/agent-guild/blob/main/docs/PORTABILITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local filesystem procedures and CLI commands for shared agent memory, onboarding, handoff, logging, portability, and maintenance.]

## Skill Version(s):

3.9.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
