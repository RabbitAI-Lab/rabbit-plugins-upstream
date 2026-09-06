## Description:

Provides Chinese-language guidance for choosing whether an agent constraint belongs in hooks, permissions, AGENTS.md or CLAUDE.md, a skill, a path-scoped rule, or the current prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to decide how to implement and govern persistent agent constraints, especially when editing AGENTS.md, CLAUDE.md, hooks, permissions, skills, or path-scoped rules. It helps route constraints to deterministic enforcement, always-on instructions, on-demand guidance, or the current session based on risk and scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional SessionEnd hook creates persistent local session metadata, including working directory, session ID, end reason, and transcript path.

Mitigation: Install the hook only after reviewing the script and confirming that this metadata is acceptable to retain locally.

Risk: The hook is a persistent local configuration change and may continue logging future sessions until removed.

Mitigation: Register it deliberately, verify it with a test session, and remove the SessionEnd entry from Claude settings when cross-session review data is no longer needed.

Risk: Guidance about hooks and permissions can be misapplied if copied across agents with different enforcement semantics.

Mitigation: Use the Claude Code-specific examples only for Claude Code and adapt the higher-level constraint-layering approach for other agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snowsonz/skills/agent-constraints)
- [Evidence summary](artifact/EVIDENCE.md)
- [Layer 1 enforcement guidance](artifact/LAYER1-ENFORCEMENT.md)
- [Layer 2 instruction guidance](artifact/LAYER2-INSTRUCTIONS.md)
- [Layer 3 on-demand guidance](artifact/LAYER3-ONDEMAND.md)
- [Session logging hook documentation](artifact/hooks/README.md)
- [AGENTS.md template](artifact/templates/AGENTS.md)
- [Evaluation cases](artifact/evals/evals.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with decision tables, inline shell commands, JSON configuration examples, and template files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily Chinese-language prose; optional hook produces a local tab-separated session log.]

## Skill Version(s):

0.1.5 (source: evidence.json release.version and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
