## Description:

Turn a YouTube link or a pasted transcript into a Chinese spoken script and a remake structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to turn a pasted transcript, or optionally looked-up public YouTube captions and comments, into a Chinese spoken remake script and structure while preserving source attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to Beatra and stores a shared device bearer token with broader account authority than captions alone require.

Mitigation: Install only when the publisher and Beatra account lifecycle are trusted; keep the credential private and use the bundled uninstall flow when removing the package.

Risk: Optional caption, video metadata, and comment lookups can spend Beatra credits.

Mitigation: Require a separate confirmation for every lookup, quote the live credit price before execution, and use stable request IDs to avoid duplicate charges during recovery.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Review the update posture before installing and disable automatic updates with the bundled update command when silent replacement is not acceptable.

Risk: A generated remake script may include unsupported claims if the source transcript is missing or incomplete.

Mitigation: Write only from looked-up captions or user-supplied transcript text, label source attribution, and mark remake-beat reasoning as inference.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/youtube-caption-studio)
- [Beatra skill homepage](https://beatra.ai/skills/youtube-caption-studio)
- [Looking up captions](references/caption-lookup.md)
- [Writing the script](references/script.md)
- [Caption studio workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown containing a Chinese spoken script, remake structure, source attribution, and optional lookup task and billing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional paid lookups return task status and billing.net_charged_credits when present; the script stage can run from a user-supplied transcript at no lookup cost.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
