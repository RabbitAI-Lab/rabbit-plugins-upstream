## Description:

Safely operates JavDB through the javdb-cli binary for discovery, authenticated lists, and explicit state changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to direct an agent to search JavDB records, inspect details, rankings, tags and lists, and perform authenticated account or watch-state actions only after explicit authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login flows can store JavDB credentials locally.

Mitigation: Run authentication only after explicit user authorization, never read or echo stored credential files, and avoid repeating passwords in responses.

Risk: Reverse image search may upload user-provided images to a configured search source.

Mitigation: Explain the upload and privacy impact before running image search, and proceed only when the user has requested it.

Risk: Marking, unmarking, account selection, configuration changes, downloads, installs, and updates can change remote state, local state, or local files.

Mitigation: Require explicit per-operation authorization and confirm targets or output paths before executing state-changing commands.

## Reference(s):

- [javdb-cli homepage](https://github.com/FlanChanXwO/javdb-cli)
- [Authentication guidance](references/auth.md)
- [Discovery workflow](references/discover.md)
- [Installation guidance](references/install.md)
- [State-change guidance](references/state.md)
- [Troubleshooting guidance](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose javdb command invocations; state-changing, install, update, download, and authentication actions require explicit user authorization.]

## Skill Version(s):

0.7.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
