## Description:

Complete TODO.md items nested under the level 2 header "Current", then update documentation, CHANGELOG.md, and manifest files according to the version update each item indicates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhauga](https://clawhub.ai/user/jhauga)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to work through repository TODO.md items, apply associated version updates, update documentation and release files, maintain a current roadmap, and archive completed TODO items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad repository changes across roadmap, documentation, changelog, and manifest files.

Mitigation: Review proposed changes before applying them and require explicit approval before writing release or manifest updates.

Risk: The fallback rollback behavior can run a workspace-wide git restore command that may discard uncommitted work.

Mitigation: Remove or replace the fallback with targeted, user-confirmed reverts and check the workspace state before rollback.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and repository file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update TODO.md, CHANGELOG.md, documentation, manifests, and .github/current.roadmap.md.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
