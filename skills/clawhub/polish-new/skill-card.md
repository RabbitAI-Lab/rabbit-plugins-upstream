## Description:

Pre-release code review that converges - runs checks, launches parallel review agents (cleanliness, design, efficiency, side-effect gating) sized to the diff, validates findings against reproducible evidence in a run ledger, fixes on approval, then reviews its own fixes until a round warrants no edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to run a structured pre-release review before committing or pushing code changes. It coordinates checks, diff scoping, review lenses, finding validation, approved fixes, and follow-up fix review until no further edits are warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be triggered by broad natural-language requests.

Mitigation: Narrow activation to `/polish-new` when installing or configuring the skill.

Risk: The skill can write run artifacts, edit ignore metadata, run checks, spawn review agents, and modify code.

Mitigation: Require explicit approval before any code or ignore-file changes, including fixes for pre-existing check failures and follow-up fix-review edits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/polish-new)
- [Project Homepage](https://github.com/tenequm/skills/tree/main/skills/polish-new)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown review report with command snippets, run-ledger files, agent reports, and targeted repository edits when approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .agents/polish run artifacts, update ignore metadata, run project checks, spawn review agents, and modify code during approved fix passes.]

## Skill Version(s):

0.1.1 (source: frontmatter metadata, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
