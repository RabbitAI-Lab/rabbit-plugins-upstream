## Description:

Seven offline mechanisms against slow, stale, zombie, and sycophantic agent turns: prompt compaction, request fencing, zombie detection, CAPTCHA triage, anti-sycophancy spine, delivery register, and invention quarry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to preflight each turn, compact prompts, fence stale generations, assess long-context hygiene, triage verification friction, and keep answers grounded under pressure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill broadly changes how an agent handles turns, disagreement, style, and unsolicited creative additions.

Mitigation: Install it only for workflows that want those behavior changes, and review generated turn guidance before relying on it in user-directed or tightly scoped workflows.

Risk: Shared local state can mix signals between agents when a common state directory is used.

Mitigation: Set ARENA_AGENT per agent so state is isolated under an agent-specific namespace.

Risk: The self-test script includes destructive resets intended for a mock HOME sandbox.

Mitigation: Run self-tests only with an isolated test HOME or the provided sandboxed test setup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-turn-accelerator)
- [Integration guide](docs/INTEGRATION.md)
- [Evidence notes](docs/evidence.md)
- [Problem analysis](docs/problems.md)
- [Machine manifest](manifest.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces per-turn preflight bundles, compact brief lines, schema output, and local state guidance; no network access or sudo is described.]

## Skill Version(s):

2.1.6 (source: server release metadata; artifact files also contain 2.1.5.1 and 2.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
