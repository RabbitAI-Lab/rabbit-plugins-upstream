## Description:

Duplicate any work-in-progress into an independent branch — not just conversations, but tasks, plans, code, writing and research. Context, confirmed conclusions, completed steps and tool results all come along; resume from any point while the original line stays untouched and keeps running. Note that a fork copies the session context only; workspace artifacts are not rolled back — unless they are version-controlled (e.g. git), only their final state exists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamingmou](https://clawhub.ai/user/yamingmou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and people working in supported coding agents use Session Fork to copy a session's context through a chosen point into an independent branch, then continue work without changing the original session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The repair command can alter original sessions, and branches can lose or change important history.

Mitigation: Back up session stores independently, specify the source session ID, inspect a dry run, and avoid WorkBuddy --fix on original or active sessions; wait for preservation fixes before using important sessions.

Risk: Copied session history and database backups may contain private information.

Mitigation: Protect session copies and backups as private data, and check that copied history and artifact references remain accurate.

## Reference(s):

- [English overview](https://github.com/yamingmou/session-fork-core/blob/main/README.en.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Session history and index files created by the bundled Python script, with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates an independent session branch through the selected point; workspace artifacts are not rolled back.]

## Skill Version(s):

2.4.22 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
