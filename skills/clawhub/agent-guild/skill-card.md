## Description:

Enables local, cross-agent sharing of identity, rules, memory, and handoff messages through a plaintext directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT

## Use Case:

People and developers using multiple AI agents share persistent preferences, project context, daily logs, and handoffs across agents on a local machine, with files designed to be moved between devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared memory can expose sensitive information to other local agents.

Mitigation: Do not store secrets in shared memory; review what each agent can read and write.

Risk: Adopting or linking skill directories can move files or alter agent installs.

Mitigation: Review dry-run output before using adopt, link-root, or port with --apply.

Risk: Network self-updates and remote installation can run unreviewed code.

Mitigation: Avoid curl-to-bash installation when possible and leave auto-upgrade in check/off rather than apply mode.

Risk: A Windows PowerShell path-escaping issue creates a command-injection risk when grooming untrusted shared archive filenames.

Mitigation: On Windows, avoid grooming untrusted shared archive filenames until the path-escaping issue is fixed.

## Reference(s):

- [Agent Guild project homepage (skill metadata)](https://github.com/dqsjqian/agent-guild)
- [Agent Guild on ClawHub](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Protocol specification](references/SPEC.md)
- [Onboarding guide](references/ONBOARDING.md)
- [Security disclosure](references/SECURITY.md)
- [Cross-device portability](references/PORTABILITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plaintext and Markdown files with command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shared data is stored locally as Markdown and JSON.]

## Skill Version(s):

3.11.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
