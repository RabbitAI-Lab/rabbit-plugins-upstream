## Description:

ChatGPT Exporter helps a user export their own ChatGPT conversation history through browser relay, bookmarklet, or token-based shell paths and write local JSON and Markdown files after explicit consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to back up or inspect their own ChatGPT conversation history locally. It supports index-only exports for titles and timestamps, or full plaintext exports when the user explicitly accepts the sensitivity risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exports can include full plaintext ChatGPT conversation history, including credentials, personal information, or confidential work material.

Mitigation: Prefer index-only mode, choose a local non-synced destination, keep file permissions restrictive, and delete exports after use.

Risk: The shell path can use a ChatGPT access token, which should be treated as sensitive account access.

Mitigation: Prefer the browser relay or bookmarklet paths when possible; if the shell path is needed, use the hidden prompt or protected environment handling and never pass a token on the command line.

Risk: The security summary flags the cleanup option as needing review because it can delete more local files than the chosen export folder.

Mitigation: Avoid --purge until the target selection is reviewed or fixed; manually delete known export folders only after checking the path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/chatgpt-exporter)
- [ClawHub publisher profile](https://clawhub.ai/user/globalcaos)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Local JSON and Markdown exports, plus command and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports may contain sensitive plaintext conversation data; index-only mode avoids fetching message bodies.]

## Skill Version(s):

1.8.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
