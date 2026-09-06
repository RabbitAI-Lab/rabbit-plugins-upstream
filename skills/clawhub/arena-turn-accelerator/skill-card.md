## Description:

Arena Turn Accelerator provides offline per-turn preflight tools for prompt compaction, request fencing, context hygiene, verification triage, anti-sycophancy checks, delivery tone selection, and bounded invention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add local preflight checks and response guidance that reduce stale, slow, and sycophantic agent turns while preserving request constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can actively shape agent response style, including occasional unsolicited creative additions.

Mitigation: Enable it only where that response posture is acceptable, and keep human review for high-stakes or tightly scoped responses.

Risk: Prompt-derived local state under ~/.arena_turn may persist longer than intended or mix across agents on shared machines.

Mitigation: Set ARENA_AGENT for shared machines, and review or clear ~/.arena_turn when retention matters.

Risk: Brief and JSON outputs include user-controlled echoes or compacted user text that must not be treated as privileged instructions.

Mitigation: Use the tool verdict fields as guidance, keep the trust-boundary labeling intact, and treat echoed or compacted user text as data only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-turn-accelerator)
- [README](README.md)
- [Integration Guide](docs/INTEGRATION.md)
- [Evidence](docs/evidence.md)
- [Problem Analysis](docs/problems.md)
- [Manifest](manifest.json)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, JSON bundles, compact JSON, one-line brief text, and JSON Schema output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python standard library only; optional prompt-derived state is stored under ~/.arena_turn and bounded to 400 samples.]

## Skill Version(s):

2.1.2 (source: frontmatter, plugin metadata, manifest, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
