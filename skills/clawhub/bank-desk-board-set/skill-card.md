## Description:

Turn user-supplied branch window names and board lines into a four-to-eight still bank desk board set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn already approved bank branch window names and board lines into a coordinated still-image desk board pack, with one still per named window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad persistent Beatra account credential and uses it for remote MCP tool calls.

Mitigation: Install only when the user trusts Beatra with that account access, keep the credential private, avoid shared machines, and use the bundled uninstall workflow or Beatra Console revocation when access is no longer needed.

Risk: Automatic updates are enabled by default and can replace package-owned code without a separate confirmation.

Mitigation: Use the documented update controls to disable automatic checks when required, and rely on the packaged verification flow that checks discovery data, archive checksums, manifest data, and file hashes before replacement.

Risk: Optional reference images are uploaded to Beatra, which can expose sensitive source material to the Beatra upload and storage path.

Mitigation: Upload only reference media the user is comfortable sending to Beatra and avoid sensitive images unless that storage path is acceptable.

Risk: Image generation consumes Beatra credits, and final measured usage can differ from the prepaid estimate.

Mitigation: Show the production card before billable work, read the live model price, submit one approved still per request identity, and report returned billing.net_charged_credits after task completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/bank-desk-board-set)
- [Beatra skill homepage](https://beatra.ai/skills/bank-desk-board-set)
- [Bank desk board pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and returned image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one still per named window, normally four to eight stills and capped at eight; paid generation is submitted one still per request.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
