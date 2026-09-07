## Description:

Turn a written holiday homework list into one holiday homework voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers and education content creators use this skill to convert an existing holiday homework assignment list into 8 to 20 labeled voice clips. It plans the clip list, requests live Beatra model and billing details, and returns generated audio task results without inventing homework items or grades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests a shared Beatra device credential with broad account powers beyond homework voice generation.

Mitigation: Review the approval scopes before installation, keep the credential local, and use the bundled client only for the documented holiday homework voice workflow.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates after installation with `python3 scripts/mcp_client.py update --auto off` when package changes require manual review.

Risk: Speech synthesis and voice cloning can consume Beatra credits.

Mitigation: Show a separate approval card for clone and speech stages, use live price and balance data, submit each paid request once with an opaque `client_request_id`, and rely on task polling for recovery.

Risk: A cloned teacher voice can create likeness and consent concerns.

Mitigation: Clone only when the teacher wants it, has likeness rights, and provides an authorized sample; treat file access alone as insufficient consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/holiday-homework-voice)
- [Holiday homework voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets; generated audio files are returned as Beatra task artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Beatra asynchronous task IDs, live billing fields, and returned audio metadata for generated clips.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
