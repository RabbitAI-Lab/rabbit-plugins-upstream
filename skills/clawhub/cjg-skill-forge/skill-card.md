## Description:

Skill Forge helps developers create, upgrade, review, consolidate, and clarify WorkBuddy/AI agent skills using guided workflows, quality rubrics, local scripts, and feedback-loop tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use Skill Forge to build new agent skills, improve existing skills, audit skill quality, consolidate overlapping local skills, and make skill instructions easier for agents to follow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill keeps local usage signals by default.

Mitigation: Review the local signal controls before use and disable local recording if that behavior is not acceptable.

Risk: Cloud upload can send anonymous feedback signals when explicitly enabled.

Mitigation: Keep cloud upload disabled unless intentionally opting in, verify the .cloud_optin state, and review cloud_config.json endpoints before enabling sync.

Risk: The skill can propagate telemetry tooling into skills it creates.

Mitigation: Review generated skills for signal tooling and disclosure text before publishing or deploying them.

Risk: Proposal, registration, or semantic commands may depend on environment settings or tokens.

Mitigation: Avoid running those commands with untrusted environment variables or tokens, and review command effects before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Introduction](artifact/references/intro.md)
- [Forge Modes](artifact/references/forge-modes.md)
- [Forge Disciplines](artifact/references/forge-disciplines.md)
- [Skill Writing Guide](artifact/references/skill-writing-guide.md)
- [Skill Review Rubric](artifact/references/skill-review-rubric.md)
- [Skill Consolidation](artifact/references/skill-consolidation.md)
- [Signals Specification](artifact/references/signals.md)
- [Cloud Configuration Schema](artifact/references/cloud-config-schema.md)
- [Security Audit](artifact/references/security-audit.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and generated or modified skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local skill files and local signal logs when its workflows are followed.]

## Skill Version(s):

3.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
