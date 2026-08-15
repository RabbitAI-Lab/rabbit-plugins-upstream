## Description:

GitX helps AI coding agents manage Git workflows, including commits, branches, checks, pull requests, issues, conflict resolution, status summaries, history views, and secret scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[musoyangrigor](https://clawhub.ai/user/musoyangrigor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use GitX with Agent Skills-compatible coding agents to inspect repository state, plan and create clean commits, manage branches, run checks, publish pull requests or issues, scan for secrets, and resolve Git conflicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-oriented workflows can change local Git history, publish code, or create public or project-visible GitHub content.

Mitigation: Review commands before using push, pull request creation, issue creation, amend, or conflict-resolution workflows, and use read-only status, plan, tree, or scan workflows when inspection is sufficient.

Risk: Commits may accidentally include secrets, credentials, private keys, logs, build artifacts, or other sensitive files.

Mitigation: Run the scan workflow and review warnings before including risky files such as .env files, keys, credentials, tokens, logs, dist, build, or node_modules content.

Risk: Conflict resolution and amend flows can alter repository state in ways that are hard to undo after publication.

Mitigation: Require explicit user confirmation for amend operations, avoid force-push behavior, and review resolved files and checks before completing merge or rebase operations.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/musoyangrigor/gitx-skill/tree/main/gitx)
- [ClawHub skill page](https://clawhub.ai/musoyangrigor/skills/gitx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with inline shell commands and generated GitHub issue or pull request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify Git repository state when the user invokes write-oriented workflows]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
