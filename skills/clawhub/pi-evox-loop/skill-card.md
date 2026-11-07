## Description:

Give your coding agent an 'experience inheritance' runtime: recall validated fixes from an Evolver gene store at task start, register hits when a fix is actually used, and deposit newly-learned fixes after repairing a non-obvious failure. Optionally run controlled closed-loop experiments (R1 trap → distill → inject → R2) to measure inheritance gains. Every fix is traced to its model/host and checked across models. Use at the START of non-trivial tasks, after fixing a non-obvious failure, or when you want to measure agent self-evolution. Trigger words: 经验召回, 错题本, 经验继承, 自进化, evolver, 避坑, distill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to recall previously validated fixes at the start of coding tasks and record useful fixes after resolving non-obvious failures. It can also guide optional controlled experiments that measure whether those fixes help across runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this skill suspicious with high confidence because it reports serious privacy, workspace-safety, and approval weaknesses, alongside undeclared capabilities; incomplete inspection leaves some evidence unresolved.

Mitigation: Treat this as a meaningful risk review, not a finding that the author is malicious. Consider avoiding installation, especially if you would use the optional agent integration, sharing features, or experimental workflows. If you still consider it, first review the flagged behaviors and account for the incomplete scan; this verdict does not establish that all content was fully inspected.

## Reference(s):

- [Pi EvoX Loop release page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Pi EvoX Loop project documentation](https://github.com/stwhwing/pi-evox-lab)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific steps; may include optional setup or experiment instructions.]

## Skill Version(s):

0.38.0 (source: server-resolved release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
