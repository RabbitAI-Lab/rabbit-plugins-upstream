## Description:

Run a structured code review (Codex default, Claude optional) as a closeout check on a local or PR branch before commit or ship.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thanosbao](https://clawhub.ai/user/thanosbao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run structured code review on local changes, commits, branches, or PR-style diffs before commit or ship. It helps coordinate reviewer output, focused tests, and follow-up verification until no accepted actionable findings remain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review helper can send repository diffs, untracked files, optional datasets, and prompt files to configured external AI review tools.

Mitigation: Use it only on repositories and files that are appropriate to share with the configured reviewer, keep secrets and private data out of included files, and use --no-web-search where possible.

Risk: The optional parallel test path executes a user-supplied shell command.

Mitigation: Use --parallel-tests only with commands you explicitly trust and review the command before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thanosbao/skills/autoreview)
- [Publisher profile](https://clawhub.ai/user/thanosbao)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown review summary with optional validated structured JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write human-readable output or structured JSON when the user supplies output paths; otherwise writes review results to stdout.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
