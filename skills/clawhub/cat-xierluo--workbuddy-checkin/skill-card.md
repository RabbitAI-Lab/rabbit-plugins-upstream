## Description:

WorkBuddy Check-in helps an agent run local scripts that read the current WorkBuddy desktop login session and call the official daily check-in API to claim daily credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users use this skill to automate their own daily check-in and credit collection from a locally logged-in desktop session. Agents can use it to run one-off checks or help configure scheduled local execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a full WorkBuddy login token through stdout and command-line headers, creating meaningful local exposure risk.

Mitigation: Install only if the publisher is trusted with the current WorkBuddy account session; avoid running decrypt-token.js directly and avoid capturing script output in shared logs.

Risk: Using automatically installed Electron runtimes expands the local supply-chain trust boundary.

Mitigation: Prefer manually supplied trusted Node or Electron runtimes, and enable automatic Electron installation only when the npm source and network path are trusted.

Risk: The skill uses the current local WorkBuddy session to act on the user's account.

Mitigation: Use it only for the current user's own account and review the WorkBuddy terms and account state before scheduling repeated execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/workbuddy-checkin)
- [Dependencies reference](references/dependencies.md)
- [WorkBuddy website](https://www.codebuddy.cn/work/)
- [Tencent Copilot API host](https://copilot.tencent.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local setup, check-in, and scheduling guidance; script logs record check-in results without token text according to the artifact documentation.]

## Skill Version(s):

1.0.2 (source: server evidence, frontmatter, changelog released 2026-08-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
