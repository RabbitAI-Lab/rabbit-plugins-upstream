## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run structured multi-round code review, apply atomic fixes, coordinate approved larger changes, validate results, and produce review summaries before release or merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated code-changing workflows can produce unexpected repository changes, especially when merge or push options are enabled.

Mitigation: Keep auto_merge and push_per_round disabled unless repository integration is explicitly desired, then review the generated branch and decision log before merging or pushing.

Risk: The skill can run configured validation commands and perform git operations during normal iteration.

Mitigation: Install and run it only in repositories where this level of agent autonomy is acceptable, and keep validation commands limited to trusted project checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Iterate README](artifact/README.md)
- [Iterate skill instructions](artifact/SKILL.md)
- [Configuration schema](artifact/config/config.schema.json)
- [Onboarding playbook](artifact/templates/onboarding-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code edits, shell commands, configuration files, and review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write project files, run configured validation commands, and create local iterate branches when used in normal mode; review-only mode emits findings and reports without modifying files.]

## Skill Version(s):

2.3.14 (source: SKILL.md frontmatter, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
