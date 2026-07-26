## Description: <br>
Git Repo guides agents through Git repository and worktree management with SourceGit integration, including ghq cloning, repository conversion, multi-account credentials, conflict dry runs, and local cleanup workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to manage local Git repositories, worktrees, ghq layouts, SourceGit registration, and GitHub multi-account access. It is intended for agent-assisted repository maintenance where the agent proposes or runs shell commands and configuration edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect persistent local Git state, including repository moves, worktree metadata, and SourceGit preferences. <br>
Mitigation: Require explicit confirmation before repository moves, metadata rewrites, SourceGit preference edits, or deletions, and inspect current status before making changes. <br>
Risk: Credential workflows can expose or persist sensitive GitHub authentication behavior if followed carelessly. <br>
Mitigation: Prefer credential-helper or SSH flows, back up git configuration before changes, and avoid token-in-URL cloning unless the remote is immediately sanitized. <br>
Risk: Some workflows proceed automatically, including cloning and SourceGit registration when conditions match. <br>
Mitigation: Ask for user approval before cloning or writing application configuration, especially in private repositories or multi-account environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/git-repo) <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [ghq Clone](clone.md) <br>
- [Credential Helper](credential-helper.md) <br>
- [SourceGit Integration](sourcegit.md) <br>
- [Worktree](worktree.md) <br>
- [To Bare](to-bare.md) <br>
- [To Ghq](to-ghq.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code] <br>
**Output Format:** [Markdown guidance with bash command blocks and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include file edits or repository operations when the user approves the workflow.] <br>

## Skill Version(s): <br>
0.6.0 (source: release metadata and changelog, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
