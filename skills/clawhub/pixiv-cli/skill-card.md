## Description:

Operate Pixiv with explicit scope and safe credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Pixiv users use this skill to search and inspect Pixiv works, users, feeds, and rankings, run reverse image searches, and carry out explicitly authorized account, curation, comment, and download actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exports may contain plaintext secrets.

Mitigation: Use private stdin or a secret manager, and keep tokens and export bundles out of chat, logs, and diagnostics.

Risk: Account actions and downloads can change account state or write files.

Mitigation: Approve the exact account action and download destination before execution.

Risk: Reverse image search may send an image to external providers.

Mitigation: Share only images authorized for submission to SauceNAO or ascii2d.

Risk: Remote MCP access exposes a server interface to clients.

Mitigation: Use trusted clients for remote MCP access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flanchanxwo/skills/pixiv-cli)
- [Pixiv CLI project documentation](https://github.com/FlanChanXwO/pixiv-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Concise text or Markdown summaries, command-line output in text/JSON/NDJSON, and downloaded files when requested.]

**Output Parameters:** [Varies by requested operation.]

**Other Properties Related to Output:** [Results and files depend on the selected Pixiv operation, account access, and requested output mode.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
