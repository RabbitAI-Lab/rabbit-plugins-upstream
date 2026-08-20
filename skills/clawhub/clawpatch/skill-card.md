## Description:

This skill teaches an agent when and how to use the Clawpatch CLI for whole-repository automated review, findings triage, and controlled per-finding fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when Clawpatch is explicitly requested, to run repository review, interpret findings, select a safe fix workflow, and avoid known CLI workflow pitfalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository contents may be sent to the selected provider CLI during review or fixes.

Mitigation: Use Clawpatch only when intended, review the configured provider and model, and keep provider authentication under user control.

Risk: Fix and PR workflows can change repository files or publish proposed changes.

Mitigation: Require explicit user approval for repo changes, PR creation, `.gitignore` edits, and any force option; review generated diffs before shipping.

Risk: Parallel fix work can corrupt shared Clawpatch state or apply patches in the wrong worktree.

Mitigation: Use scanner-only mode for parallel fixes, dispatch each finding in a fresh worktree, and never run `clawpatch fix` from parallel subagents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tmchow/skills/clawpatch)
- [Clawpatch homepage](https://clawpatch.ai)
- [Publisher profile](https://clawhub.ai/user/tmchow)
- [clawpatch npm package](https://www.npmjs.com/package/clawpatch)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON field references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes provider configuration notes, review and fix workflow selection, and command safety guidance.]

## Skill Version(s):

0.1.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
