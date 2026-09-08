## Description:

Exports a user's ChatGPT conversation history to local JSON and Markdown files, with index-only defaults, consent prompts, and browser-based or token-based access paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to back up, inspect, or migrate their own ChatGPT conversation history while choosing between index-only metadata exports and full-content exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exports may store sensitive ChatGPT conversation history as plaintext local files.

Mitigation: Prefer index-only mode unless message bodies are required, export to a private non-synced folder, and delete local exports when no longer needed.

Risk: The headless token path requires access to a ChatGPT session bearer token.

Mitigation: Prefer the browser relay or bookmarklet paths, use a hidden prompt instead of environment variables when possible, and never pass tokens as command-line arguments.

Risk: Security evidence reports that the purge command can delete more local data than the documentation claims.

Mitigation: Avoid using --purge until deletion target validation has been reviewed and fixed, and inspect the target path before any destructive cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/chatgpt-exporter-ultimate)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [ChatGPT web application](https://chatgpt.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Local plaintext JSON and Markdown export files, plus command-line and browser execution guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Index-only mode avoids fetching message bodies; full exports can include sensitive conversation text and metadata.]

## Skill Version(s):

1.8.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
