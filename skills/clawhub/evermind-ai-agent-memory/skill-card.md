## Description:

Cross-session memory recovery for AI agents that uses local discovery, always-loaded core memory, hash-indexed conditional reads, and handover notes so agents can resume work without rereading every memory file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Evermind to recover identity, rules, todos, work logs, and recent handover state at the start of a new session. It is intended for local agent memory workflows where the agent should avoid cold starts and reduce repeated context reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill can add persistent rule enforcement and broad local file-write behavior.

Mitigation: Review the release artifact and generated .evermind files before deployment, and enable hook-based enforcement only after confirming the rules are expected.

Risk: The skill reads and indexes local memory files that may contain private rules, handovers, or user context.

Mitigation: Keep .evermind outputs out of shared commits when they contain private data, and install only in projects whose memory files are trusted.

Risk: Untrusted config.yaml output paths could cause unexpected local file writes.

Mitigation: Avoid running the indexer with untrusted configuration and prefer pinned ClawHub artifacts over cloning a moving default branch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ccy123abcd/skills/evermind-ai-agent-memory)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Example configuration](config.example.yaml)
- [Handover template](assets/handover-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text guidance with shell commands, JSON rule data, YAML configuration, and generated local memory-index files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local files such as memory_index.md, memory_index_state.json, .evermind/discovery.json, optional .evermind/rules.json, and optional .evermind/handover.md.]

## Skill Version(s):

0.4.3 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
