## Description:

Turn a vertical short-drama episode script into a labeled short drama voiceover pack with one consistent voice per role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and production teams use this skill to turn attributed vertical short-drama episode scripts into ordered, labeled voiceover clips with consistent voices per role. It also supports optional consent-gated role voice cloning and Beatra task recovery for paid speech generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports a broad shared Beatra Device Token and a suspicious verdict.

Mitigation: Review the skill before sensitive use, keep the token only in the documented local credential file, and avoid exposing credentials in logs, prompts, command arguments, or copied files.

Risk: Security evidence reports silent automatic code updates by default.

Mitigation: Disable automatic updates when reviewed code must remain fixed, then perform explicit update checks before accepting a newer release.

Risk: Paid voice cloning and speech synthesis can create duplicate charges if uncertain requests are resent with changed identifiers.

Mitigation: Use one stable client request ID per paid block, poll existing tasks through terminal status, and retry only identical frozen payloads after recovery.

Risk: Voice cloning can misuse a speaker sample without authorization.

Mitigation: Require explicit consent attestation before uploading a sample or creating a clone request, and treat file access alone as insufficient consent.

## Reference(s):

- [Short-drama voice-pack workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/short-drama-voice-pack)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces episode cast and line ledgers, Beatra task polling guidance, labeled audio clip result reporting, and recovery instructions; the generated audio artifacts are produced by the connected Beatra service.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
