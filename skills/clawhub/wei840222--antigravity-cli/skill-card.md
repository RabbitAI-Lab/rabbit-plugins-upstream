## Description:

Provides guidance for using the Antigravity CLI (agy), including interactive and headless workflows, configuration, permissions, plugins, artifact review, migration, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wei840222](https://clawhub.ai/user/wei840222)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to operate the Antigravity CLI for interactive sessions, one-shot prompts, configuration, permissions, plugins, and artifact review. It also helps diagnose common installation, authentication, and updater issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Headless runs may edit workspace files without an interactive approval prompt.

Mitigation: Limit CLI access to the intended project, keep permission bypass off, and review generated changes.

Risk: Downloaded installers execute commands on the user's system.

Mitigation: Review installers before running them.

Risk: Removing an updater lock while an update is active could disrupt that update.

Mitigation: Confirm no update is running before removing a lock, then restore automatic updates or maintain manual updates.

Risk: Prompts may share project content with the configured AI provider.

Mitigation: Share only project content appropriate for that provider.

## Reference(s):

- [CLI Usage](artifact/references/cli-usage.md)
- [Headless CLI](artifact/references/headless.md)
- [Command Reference](artifact/references/command-reference.md)
- [Security and Permissions](artifact/references/security-permissions.md)
- [Artifact Review](artifact/references/artifacts.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Official CLI Reference](https://antigravity.google/docs/cli/reference/)
- [Official CLI Best Practices](https://antigravity.google/docs/cli/best-practices/)
- [Official CLI Installation](https://antigravity.google/docs/cli-install)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI flags and defaults are version-dependent; verify the installed agy binary.]

## Skill Version(s):

2026.11.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
