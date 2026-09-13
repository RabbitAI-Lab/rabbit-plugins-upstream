## Description:

Pre-release code review that converges - parallel review agents sized to the diff, findings validated against evidence in a run ledger, fixes on approval, then re-reviews its own fixes until a round warrants no edits. Run on /polish-new.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before release to run a structured code review over a diff, validate findings against reproducible evidence, apply approved fixes, and re-review those fixes until no new edits are warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may change the working tree before the final approval step.

Mitigation: Run it in a clean branch or disposable worktree and inspect all diffs before accepting the results.

Risk: The workflow may fix unrelated pre-existing lint or type-check failures and modify ignore files.

Mitigation: Review the complete working-tree diff and separate unrelated fixes before committing.

## Reference(s):

- [polish-new homepage](https://github.com/tenequm/skills/tree/main/skills/polish-new)
- [polish-new on ClawHub](https://clawhub.ai/tenequm/skills/polish-new)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown review reports, ledger files, code diffs, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create review run artifacts and modify repository files during checks or approved fixes.]

## Skill Version(s):

0.1.2 (source: frontmatter, release evidence, changelog; released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
