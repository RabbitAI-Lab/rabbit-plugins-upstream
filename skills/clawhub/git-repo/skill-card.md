## Description: <br>
Git repository and SourceGit integration for cloning, worktree inventory and reuse, repository conversion, conflict dry runs, duplicate cleanup, and multi-account SSH or HTTPS credential setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to manage local Git repositories, ghq layouts, SourceGit registration, worktrees, repository migration, and multi-account GitHub access. It is intended for repository maintenance workflows where an agent proposes or runs Git and filesystem operations with human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can alter local repositories, worktree metadata, SourceGit preferences, and Git credential behavior. <br>
Mitigation: Require explicit confirmation for migration, duplicate cleanup, SourceGit sync, patrol cleanup, and credential-helper topics before applying changes. <br>
Risk: Repository migration or metadata rewrites can target the wrong path or damage worktree state. <br>
Mitigation: Verify every source and target path, inspect repository status first, and back up relevant configuration before allowing deletes, moves, or metadata rewrites. <br>
Risk: Credential-helper workflows can expose or pin credentials incorrectly. <br>
Mitigation: Avoid token-in-URL cloning and review per-organization credential-helper changes before writing Git configuration. <br>
Risk: SourceGit configuration edits can be overwritten or corrupt local GUI preferences. <br>
Mitigation: Back up preference.json and ensure SourceGit state is suitable before changing registration or workspace settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>
- [Worktree guide](worktree.md) <br>
- [Credential helper guide](credential-helper.md) <br>
- [SSH key guide](ssh-key.md) <br>
- [SourceGit guide](sourcegit.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and procedural checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that modify repositories, worktree metadata, SourceGit preferences, or Git credential configuration.] <br>

## Skill Version(s): <br>
0.6.1 (source: ClawHub release metadata and CHANGELOG, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
