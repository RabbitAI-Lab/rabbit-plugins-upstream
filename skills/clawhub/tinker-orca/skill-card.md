## Description:

TinkerClaw ORCA drafts independent code changes in parallel, applies them with per-file serialization, and can optionally create per-unit commits after double opt-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to split multi-file coding work into independent units, run one subagent per unit through their configured OpenClaw provider, and apply the resulting patches while serializing writes to shared files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can allow automated agents to create worktrees, branches, commits, and run local git commands inside the target repository.

Mitigation: Use it only on repositories where that level of automation is acceptable, keep commits disabled unless intentionally double-confirmed, and review the resulting diffs before relying on them.

Risk: Untrusted unit IDs, paths, verification commands, or executable paths could make repository mutations broader or less predictable than intended.

Mitigation: Provide trusted unit definitions, keep each unit's writes list explicit and narrow, and pass explicit safe executable paths instead of relying on defaults.

Risk: The security summary flags under-disclosed and inconsistently scoped high-impact repository mutations and project-specific worker instructions.

Mitigation: Review the artifact carefully before installation and compare the documented permissions against the workflow behavior before using it on valuable work.

Risk: The skill spawns one subagent per edit unit through the user's configured provider, which can incur provider costs.

Mitigation: Start with a small number of units and confirm provider configuration and expected cost before larger runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/tinker-orca)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw repository link from artifact metadata](https://github.com/globalcaos/tinkerclaw)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with JavaScript workflow configuration and shell-oriented execution steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent instructions for repository-local patch application and optional per-unit commits; it does not directly produce credentials or network calls.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
