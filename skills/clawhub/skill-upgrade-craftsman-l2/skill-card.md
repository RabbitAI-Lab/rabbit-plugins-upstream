## Description:

技能升级巧匠L2 helps users systematically upgrade existing AI skills that have basic structure but suffer from routing misses, multi-skill conflicts, incomplete frontmatter, unclear boundaries, or weak handoff contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeasonhaitao](https://clawhub.ai/user/jeasonhaitao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and agent maintainers use this agent to diagnose existing Skill definitions and produce structured L2 upgrade packages that improve trigger registration, routing boundaries, multi-skill coordination, output contracts, and validation coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may overlap with other authoring or debugging skills in a crowded skill environment.

Mitigation: Narrow trigger phrases before installation so the skill activates only for existing Skill upgrades and multi-skill routing problems.

Risk: Routing behavior may vary by platform because trigger and frontmatter support depends on the deployment target.

Mitigation: Run the provided test prompts in the target platform and confirm routing before relying on the skill in a production skill group.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jeasonhaitao/skills/skill-upgrade-craftsman-l2)
- [Deployment README](artifact/README_DEPLOY.md)
- [Test Prompts](artifact/TEST_PROMPTS.md)
- [Validation Report](artifact/VALIDATION_REPORT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with SKILL.md blocks, comparison tables, test prompts, and validation templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a structured L2 upgrade package rather than executing code or calling external tools.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
