## Description:

Turn a murder-mystery or indie-game script into a labeled multi-character voice pack with one consistent voice per role and numbered clips ready for engine or tabletop use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, narrative designers, and tabletop or game creators use this skill to convert attributed scripts into cast sheets, line ledgers, and Beatra speech tasks that produce labeled character audio clips in script order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill requests broad account powers and paid generation authority.

Mitigation: Review Beatra account, privacy, and billing terms before authorizing; require explicit user confirmation of cast, block count, and cost estimate before paid speech or voice-clone calls.

Risk: The security evidence warns that use involves a persistent shared bearer token and trust in Beatra with scripts and optional voice samples.

Mitigation: Keep the token only in the private credential file, do not expose it in chat or logs, and avoid unpublished or sensitive scripts unless Beatra's terms are acceptable.

Risk: The security evidence notes that installed code can silently update by default.

Mitigation: Disable automatic updates with the bundled update control before use when change control or review of each package version is required.

Risk: The artifact supports optional voice cloning, which can create consent and misuse concerns.

Mitigation: Clone a voice only after explicit authorization from the speaker or owner, and keep each clone request tied to the disclosed consent-attested workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/game-script-voice-pack)
- [Beatra skill homepage](https://beatra.ai/skills/game-script-voice-pack)
- [Game voice-pack workflow](artifact/references/workflow.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples, shell command snippets, and task result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful generation reports numbered character-labeled clips with task status, duration, MIME type, artifact or URL, resolved model, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
