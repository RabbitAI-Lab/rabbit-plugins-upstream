## Description:

Thompson-mode discipline for any coding task: think first, build bottom-up, brute force until measured, rewrite over patch. Not for non-coding requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ken to keep coding agents focused on bottom-up implementation, small interfaces, minimal dependencies, measurement before complexity, and rewriting problematic units when warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill applies as a persistent coding-style mode and may influence later responses until disabled.

Mitigation: Use 'stop ken' or 'normal mode' when the mode should no longer affect the agent.

Risk: Rewrite-oriented guidance may be unsuitable when a task requires a conservative patch or strict preservation of existing behavior.

Mitigation: Disable the mode or explicitly request conservative patching for those tasks, then review proposed code changes before use.

Risk: Broad coding guidance can be distracting or inappropriate for non-coding requests.

Mitigation: Use the skill only for coding tasks and disable it for unrelated conversations.

## Reference(s):

- [Project homepage](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown responses with code blocks or shell commands when the coding task calls for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Code-first responses followed by concise notes about rewrites, discarded approaches, and brute-force ceilings when applicable.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
