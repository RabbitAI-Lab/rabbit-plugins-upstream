## Description:

Build a feature in an isolated worktrunk worktree, commit the changes, push the branch, and open a draft PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mertbuilds](https://clawhub.ai/user/mertbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to turn implementation requests into an isolated branch and worktree workflow. It can guide code changes through commit, push, draft PR creation, and optional dev-server startup for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can automatically create branches, copy ignored environment files, push code, open draft PRs, and start background servers from broad implementation requests.

Mitigation: Use explicit scope when invoking the skill, review the planned changes before execution, and check repository state before allowing push or PR creation.

Risk: Repositories with sensitive .env files may expose more local context to the workflow than intended.

Mitigation: Review ignored environment files before use, avoid invoking the skill in repositories with unmanaged secrets, and scan diffs before commit or push.

Risk: Background dev servers may remain running after implementation work if cleanup is missed.

Mitigation: Track any started server process and stop it when the implementation session or review loop is complete.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/mertbuilds/skills/tree/main/implement)
- [ClawHub skill page](https://clawhub.ai/mertbuilds/skills/implement)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command blocks and PR/test-plan text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose repository changes, commits, branch pushes, draft PR content, and dev-server URLs when the workflow is invoked.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
