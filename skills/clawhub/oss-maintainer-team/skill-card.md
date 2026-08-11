## Description:

Manages open source repositories by triaging issues, reviewing code, testing, releasing updates, auditing security, and maintaining documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to coordinate common open source repository maintenance work, including issue triage, pull request review, testing, release preparation, security review, and documentation updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintainer-style file and shell access can produce incorrect repository changes or unsafe commands if used without review.

Mitigation: Install only in repositories where this access is acceptable, and keep normal maintainer review controls around generated changes and commands.

Risk: Project context stored in memory may include repository details that should not be retained broadly.

Mitigation: Use the skill only where memory storage is acceptable, avoid exposing secrets, and clear or limit retained context according to the workspace policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/oss-maintainer-team)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, code changes, configuration guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read repository files, edit documentation or tests, run shell commands, and retain project context in memory when used by an agent.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
