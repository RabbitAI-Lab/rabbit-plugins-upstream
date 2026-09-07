## Description:

Turn a user-supplied geography place table and authorized stills into one geography place talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and educators use this skill to turn a teacher-provided geography place table and authorized still images into short place-fact talking clips. The workflow emphasizes one still per clip, spoken facts already present in the supplied table, and separate approval before paid voice, speech, or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with access to multiple media and account capabilities.

Mitigation: Install only when the publisher is trusted, keep the credential private, and use the documented uninstall or Beatra Console revocation path when access should be removed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use the documented update controls, including `python3 scripts/mcp_client.py update --auto off`, when silent replacement is not acceptable.

Risk: Voice, speech, and video generation can spend Beatra credits and may return final charges that differ from request-time estimates.

Mitigation: Review current model pricing and approval cards before each paid stage, submit each paid request once with an opaque request ID, and rely on task billing fields for final charges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/geo-place-talking)
- [Beatra skill homepage](https://beatra.ai/skills/geo-place-talking)
- [Geography place talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with command examples, JSON payloads, task status summaries, and generated media artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled slot list before paid work; generated audio and video results are returned as task artifacts when remote Beatra tasks succeed.]

## Skill Version(s):

0.1.2 (source: server evidence release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
