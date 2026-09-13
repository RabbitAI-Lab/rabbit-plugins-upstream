## Description:

On-demand tool client for the Uno tool gateway at agentools.uno that helps an agent search for a specific external tool, preview a planned invocation, and run a user-approved call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lxyd-ai](https://clawhub.ai/user/lxyd-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill when built-in tools do not cover a narrow real-time lookup or service action. It guides the agent through checking credentials, searching the Uno gateway, previewing the selected tool call, and proceeding only after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad external tool gateway that may access connected services or spend credits.

Mitigation: Use it only for explicit user requests, check account credits before heavier use, and require a dry-run preview plus explicit approval for every real call.

Risk: Executable behavior depends on the externally installed uno-cli PyPI package.

Mitigation: Pin and verify the uno-cli package version before use, and review upgrades before relying on new behavior.

Risk: Some artifact instructions do not consistently preserve the approval-before-call model.

Mitigation: Apply the stricter safety posture from server evidence: search, dry-run preview, user approval, then a single real call.

Risk: Write, send, purchase, key deletion, logout, and disconnect actions can affect user data, accounts, or spending.

Mitigation: Summarize the intended action in plain language and get explicit user confirmation immediately before invoking these actions.

## Reference(s):

- [Uno homepage](https://agentools.uno)
- [Uno CLI PyPI package](https://pypi.org/project/uno-cli/)
- [ClawHub skill page](https://clawhub.ai/lxyd-ai/skills/uno-cli)
- [Publisher profile](https://clawhub.ai/user/lxyd-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to show one user-visible action at a time, including dry-run preview JSON before real external calls.]

## Skill Version(s):

1.2.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
