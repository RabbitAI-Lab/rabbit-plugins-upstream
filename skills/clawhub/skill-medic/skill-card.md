## Description:

Audits installed AI skills by inventorying them, finding duplicate or conflicting behavior, scoring maturity, and recommending whether to keep, merge, improve, or remove them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, team skill maintainers, and skill ecosystem administrators use this skill to inspect workspace and global agent skills, identify overlap or conflicts, assess maturity, and produce practical cleanup recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read installed skill definitions from workspace, global, and hidden skill folders, which can expose proprietary prompts or secrets embedded in skill files.

Mitigation: Run it only in environments where installed skill definitions are appropriate to inspect, and remove secrets or proprietary prompt material from skill files before use.

Risk: The skill can save local inventories and reports under .medic, so audit results may persist after the run.

Mitigation: Review and delete .medic artifacts when the audit is complete, especially in shared workspaces.

Risk: The inspected CLI may not enforce the advertised workspace-only mode, which can make the scan broader than expected.

Mitigation: Treat workspace-only scans cautiously and verify the reported scan scope before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/skill-medic)
- [Publisher profile](https://clawhub.ai/user/songzhou666)
- [Server-resolved source repository](https://github.com/songzhou666/skill-medic)
- [Artifact README](artifact/README.md)
- [Rubric detail](artifact/references/rubric-detail.md)
- [Conflict catalog](artifact/references/conflict-catalog.md)
- [CLI guide](artifact/references/cli-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON inventories, and command-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local inventory, scoring, conflict, prescription, and report artifacts under .medic.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
