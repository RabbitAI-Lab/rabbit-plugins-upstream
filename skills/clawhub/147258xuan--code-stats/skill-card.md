## Description:

Analyze workspace code complexity, including file counts by type, line counts, language breakdown, and TODO/FIXME density.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can use this skill to review a workspace's file and line counts, language mix, and TODO/FIXME density when assessing repository size and health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review coverage is incomplete: some components were only partially inspected.

Mitigation: Consider the incomplete scan coverage when deciding whether to install, and review the skill source before use.

## Reference(s):

- [ClawHub code-stats release](https://clawhub.ai/147258xuan/skills/code-stats)

## Skill Output:

**Output Type(s):** [Analysis, Text]

**Output Format:** [JavaScript statistics object and human-readable plain-text report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Line counts cover recognized text file types; directory totals skip common dependency and generated folders. The CLI prints up to 20 TODO/FIXME/HACK/XXX matches.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact package.json reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
