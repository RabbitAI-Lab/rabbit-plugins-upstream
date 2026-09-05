## Description:

Turn a public TikTok stitch target into one quote reply card per chosen hook. This stitch prompt card studio reads the quoted video and comments, then makes quote reply stills from the reply lines you already wrote. Use it for quote reply cards, stitch prompt cards, and TikTok quote reply stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, social media operators, and agent users use this skill to turn supplied TikTok captions, comments, and prewritten reply lines into a small set of quote-reply still cards. It helps plan, price, generate, review, and recover Beatra-backed lookup and image-generation tasks without posting to TikTok.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a broad Beatra account connection with media, task, artifact, and wallet-related authority.

Mitigation: Install only when that access is acceptable, review account and device access in the Beatra console after use, and revoke the connection when it is no longer needed.

Risk: The bundled client can silently update installed package files.

Mitigation: Disable automatic updates before first use with `python3 scripts/mcp_client.py update --auto off` when manual review of updates is required.

Risk: Paid lookup and image-generation tasks can incur Beatra credits or duplicate charges if retried incorrectly.

Mitigation: Confirm lookup and generation separately, quote live prices, use one opaque `client_request_id` per unchanged paid request, and recover uncertain submissions with the same identity only when arguments are byte-identical.

Risk: Local images or private credentials could be exposed if handled outside the documented flow.

Mitigation: Inspect local files before upload, upload only through the bundled client, avoid sensitive local files, and never place the Device Token in chat, command arguments, environment variables, logs, or package files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/stitch-prompt-card)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/stitch-prompt-card)
- [Stitch prompt workflow](artifact/references/workflow.md)
- [Comment lookup](artifact/references/comment-lookup.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell and JSON examples, plus generated image artifacts returned by Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 1 to 6 quote-reply stills, confirms live pricing before paid lookup or image generation, and reports task status, artifacts, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence, manifest.json, bundled script constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
