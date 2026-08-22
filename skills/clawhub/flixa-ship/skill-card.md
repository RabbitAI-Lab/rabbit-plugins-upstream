## Description:

Ship focused repository changes with Flixa: inspect, implement, verify, and return a shareable proof of work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deniai](https://clawhub.ai/user/deniai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to carry out focused repository changes, including inspection, implementation, verification, and concise reporting. It is intended for build, fix, refactor, debug, or verification work where unrelated working-tree changes must be preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separate Flixa backend or plugin may introduce behavior outside this skill's reviewed workflow.

Mitigation: Review the Flixa backend or plugin separately before installing or pairing it with this skill.

Risk: A sharing command could publish a proof of work when the operator did not intend to share it.

Mitigation: Use `flixa share` or `flixa ship --share` only when publication is intentional, and confirm secret and absolute-path redaction before sharing.

Risk: Repository edits or shell commands can affect source files, credentials, CI settings, or deployment state.

Mitigation: Follow the skill's approval boundaries: inspect first, preserve unrelated work, and require explicit approval for destructive actions, credential changes, publishing, pushes, merges, or external-service commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deniai/skills/flixa-ship)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown final report with optional code, shell commands, configuration changes, and repository file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final response reports shipped status, summary, files changed, verification, and follow-up.]

## Skill Version(s):

0.3.0-canary.28 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
