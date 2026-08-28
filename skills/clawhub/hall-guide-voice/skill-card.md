## Description:

Turn a written hall window list into one hall guide voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service hall staff and supporting agents use this skill to turn an already-written hall window list into a labeled 8 to 20 clip voice pack, with one spoken guide clip per window cue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra connection uses a shared device credential with broad media, artifact, task, and wallet-spend capabilities.

Mitigation: Install only after reviewing the requested access, keep the credential private, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: Voice-sample uploads, voice cloning, and speech generation can affect the user's account and consume credits.

Mitigation: Require explicit approval before any clone or paid speech stage, use one opaque request identity per paid task, and report final billing from returned task fields.

Risk: Automatic updates are enabled by default and can change package code without a separate prompt.

Mitigation: Disable silent update checks with scripts/mcp_client.py update --auto off when predictable, pre-reviewed code is required.

Risk: Hall guide audio could contain invented windows, documents, approvals, eligibility results, or mispronounced names.

Mitigation: Use only the supplied written window list, stop for a pronunciation table when names are present, and review each clip against the source list before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/hall-guide-voice)
- [Beatra skill homepage](https://beatra.ai/skills/hall-guide-voice)
- [Hall guide voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Tasks and results](references/tasks-and-results.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples; successful speech tasks return audio artifact files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans a free labeled slot list before paid calls, then may submit one paid speech task per slot and one optional paid voice-clone task.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
