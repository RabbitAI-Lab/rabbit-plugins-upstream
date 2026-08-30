## Description:

Make a spoken recommendation video from a topic by selecting a script pattern, drafting separated on-screen and spoken beats, generating still frames, narration, optional music, and a short vertical clip animated from the opening frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content operators use this skill to turn a product, service, or topic into a ready-to-review short-form recommendation video workflow. It is intended for zero-footage product seeding posts, creator recommendations, review-style shorts, service explainers, and account-building content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token stored under ~/.beatra with authority to spend Beatra credits after approval gates.

Mitigation: Install only when that authorization model is acceptable, protect the credential files, require explicit approval before paid calls, and revoke the device authorization from the Beatra Console when the skill is no longer used.

Risk: The bundled client silently checks for and installs verified package updates by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` for manual update control, and review package changes before re-enabling automatic updates.

Risk: Generated recommendation videos can contain unverified claims if prices, specifications, ingredients, results, timeframes, certifications, or promotional terms are supplied incorrectly.

Mitigation: Keep unsupported claims in draft form, require the user to supply claim evidence, and review scripts before any paid generation.

## Reference(s):

- [Choosing the pattern](references/script-patterns.md)
- [Writing the spoken lines](references/spoken-lines.md)
- [Seeding video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON request payloads, task identifiers, artifact links, still images, audio tracks, and a short video file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default vertical output is 9:16 with a 12-second target and a 15-second maximum; billable Beatra generation calls require staged user approval.]

## Skill Version(s):

0.1.7 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
