## Description:

Turns a user-supplied or looked-up trending topic into publishable social content, including angle options, cover wording, caption, hashtags, optional generated media, and delivery guidance for short-form platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and social media operators use this skill to move quickly from a live topic or seasonal peg to a ready-to-publish post, with optional trend lookup and optional generated cover, narration, and short vertical video materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra device token locally with broad media and wallet-related scopes.

Mitigation: Install only when those scopes are acceptable, keep the token out of logs and prompts, and revoke the connected device from Beatra Console when the skill is no longer needed.

Risk: Silent package self-updates are enabled by default.

Mitigation: Review update behavior before installation and run `python3 scripts/mcp_client.py update --auto off` if silent updates are not acceptable.

Risk: Trend lookup and media generation can spend Beatra credits.

Mitigation: Require explicit user confirmation for each priced lookup or generation stage, report returned billing fields, and review account credit implications before use.

## Reference(s):

- [Finding the angle](references/angle-finding.md)
- [Looking up what is trending](references/trend-lookup.md)
- [Building the post](references/post-plan.md)
- [Hot topic workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Task polling, artifacts, and result fields](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with command examples, JSON payloads, social post copy, and generated media artifact links when production is approved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paid Beatra task identifiers, billing fields, model selections, media dimensions, duration, MIME type, and artifact URLs when returned by completed tasks.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
