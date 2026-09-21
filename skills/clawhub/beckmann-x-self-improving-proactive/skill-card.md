## Description:

Combination skill that adds the Beckmann Knowledge Graph as a deep-reasoning escalation layer on top of the Self-Improving + Proactive Agent, with user confirmation before escalation and memory integration afterward.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matthiasbeckmann987-spec](https://clawhub.ai/user/matthiasbeckmann987-spec)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route everyday work through the Self-Improving + Proactive Agent while offering optional Beckmann Knowledge Graph analysis for paradoxes, open scientific questions, long-horizon forecasts, strategic dead ends, AI safety questions, and epistemological limits. Confirmed Beckmann insights are reflected on and stored in the self-improving memory tiers for later reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write Beckmann-derived conclusions into cross-session memory and reuse them later.

Mitigation: Require explicit approval before saving or promoting Beckmann memory entries, and periodically review stored #beckmann entries.

Risk: The skill depends on unpinned third-party skills.

Mitigation: Review or pin ivangdavila/self-improving and matthiasbeckmann987-spec/beckmann-knowledge-graph before installation.

Risk: Memory tagged #beckmann remains after uninstall.

Mitigation: Delete or archive retained #beckmann entries from ~/self-improving if persistent memory is no longer desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/matthiasbeckmann987-spec/skills/beckmann-x-self-improving-proactive)
- [Skill README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown guidance with structured answer templates and memory-entry formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose shell-free workflow steps, graph-grounded answer sections, self-reflection entries, and memory updates.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
