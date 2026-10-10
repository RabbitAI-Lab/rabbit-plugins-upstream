## Description:

Provides durable cross-agent memory and optional browser and X session control through local tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linggen](https://clawhub.ai/user/linggen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use Linggen to save and retrieve durable preferences and decisions across sessions and hosts, and to control an authorized browser or read their logged-in X session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory may retain sensitive personal facts without an explicit save request.

Mitigation: Prefer explicit saves, avoid secrets, and regularly review and delete stored memories.

Risk: Scan and dream workflows can read prior agent transcripts.

Mitigation: Run these workflows only when authorized to read the affected sessions.

Risk: Recalled memories can reach the configured LLM provider through agent prompts.

Mitigation: Store only information appropriate to share with that provider.

Risk: First-run installation and upgrades can introduce powerful local binaries.

Mitigation: Review and approve installation and upgrades before running them.

Risk: Browser control can act in a logged-in session, and usage pings may be unwanted.

Mitigation: Use browser permissions deliberately and disable telemetry with the documented no-telemetry file if desired.

## Reference(s):

- [Linggen on ClawHub](https://clawhub.ai/linggen/skills/linggen)
- [Linggen homepage](https://linggen.dev)
- [Memory routing rules](references/routing-rules.md)
- [Dream workflow](references/dream-flow.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recalled memory and browser or X session information.]

## Skill Version(s):

2.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
