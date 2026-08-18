## Description:

Guides agents through source-building, launching, and troubleshooting DeepSeek Harness on Windows, including pnpm/corepack issues, WorkBuddy/CodeBuddy sandbox pitfalls, workspace persistence, EPERM symlinks, and port 3080 conflicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[potfromsky](https://clawhub.ai/user/potfromsky)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and support engineers use this skill to deploy and troubleshoot DeepSeek Harness from source on Windows. It is focused on practical installation, launch, workspace, and known-failure recovery guidance rather than desktop packaging or unrelated environment changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact troubleshooting steps can change process state or files under ~/.dsh when clearing NODE_OPTIONS, stopping a process on port 3080, or deleting a stale symlink.

Mitigation: Have the agent explain the exact command, scope, and expected effect, then obtain user confirmation before running those steps.

Risk: The NODE_OPTIONS workaround could be over-applied outside the DeepSeek Harness troubleshooting context.

Mitigation: Use it only for the specific dsh web launch command described by the skill, and do not make it a global or persistent environment change.

## Reference(s):

- [DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness Windows deployment pitfalls](references/deploy-pitfalls.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell and PowerShell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended to be explained to the user before high-impact troubleshooting steps are run.]

## Skill Version(s):

1.0.4 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
