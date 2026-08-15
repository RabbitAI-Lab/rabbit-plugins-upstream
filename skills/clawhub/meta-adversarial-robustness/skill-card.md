## Description:

A distilled meta-skill for adversarial robustness tasks that adds self-verification, self-reflection, super-agent orchestration, adversarial validation, and continuous learner-backed improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to support adversarial robustness work with self-verification, reflection, and learner-backed tracking of repeated failures or preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to retain cross-session notes.

Mitigation: Keep learner notes non-sensitive and periodically inspect or delete learned_patterns.json.

Risk: The skill describes automatic updates to its own instructions.

Mitigation: Require human review before accepting any SKILL.md rewrite or persistent instruction change.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON learner records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a local learned_patterns.json memory file when learner commands are run.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
