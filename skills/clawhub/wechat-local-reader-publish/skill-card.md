## Description:

Reads and decrypts the user's own local desktop WeChat databases on Windows, macOS, or Linux, masks common personal identifiers, and helps produce scheduled work summaries that can be delivered by email, WeCom webhook, or HTTP endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gp198922](https://clawhub.ai/user/gp198922)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and summarize their own local desktop WeChat messages, contacts, groups, unread messages, favorites, and chat history through a local CLI. It is intended for personal desktop data only and excludes mobile devices and other people's accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can decrypt and expose local WeChat chats, contacts, favorites, plaintext caches, and key material.

Mitigation: Install and run it only for the user's own desktop WeChat data, review outputs before sharing, use --mask and --clean where possible, and treat ~/.wechat-cli/all_keys.json plus cache files as sensitive secrets.

Risk: Sending generated summaries or exports to email, webhooks, or HTTP endpoints can disclose private message content.

Mitigation: Use only trusted destinations, apply masking before delivery, and avoid forwarding raw or unnecessary chat history.

Risk: Some setup or platform recovery paths may require elevated privileges or local environment changes.

Mitigation: Avoid privilege-changing steps unless the user understands and can reverse them; keep macOS resigning opt-in and review it before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gp198922/skills/wechat-local-reader-publish)
- [Upstream wechat-cli repository](https://github.com/freestylefly/wechat-cli)
- [Windows key extraction attribution: wcdb-key-tool](https://github.com/TANGandXUE/wcdb-key-tool)
- [wechat-decrypt reference project](https://github.com/ylytdeng/wechat-decrypt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus JSON, text, or Markdown CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands may read, decrypt, mask, export, summarize, or push local WeChat data depending on the user's workflow.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
