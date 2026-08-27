## Description:

Turn a written elder-checkup schedule into one spoken voice clip per labeled cue, delivering an 8 to 20 clip pack from the schedule the office already wrote.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Community office staff use this skill to turn an existing elder-checkup schedule into short labeled notice clips while keeping each schedule item on its own audio file. Agents use it to plan the clip list, confirm any paid voice cloning or speech synthesis step, and deliver generated MP3 voice-pack outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports broad persistent Beatra device authorization covering creative generation, tasks, artifacts, and wallet spending.

Mitigation: Authorize only in trusted agent environments, review the requested account access before use, and revoke access from the Beatra Console or the bundled uninstall workflow when finished.

Risk: The security evidence flags silent package updates, installation registration, and shared ~/.beatra credential handling as behaviors that may exceed a narrow voice-pack task.

Mitigation: Use the skill only where these behaviors are acceptable, and disable automatic update checks with `python3 scripts/mcp_client.py update --auto off` when silent updates are not desired.

Risk: The artifact can synthesize voice clips and optionally clone a staff voice, which creates consent and misuse risk.

Mitigation: Use only the supplied schedule, require explicit likeness and voice rights before cloning, collect pronunciations for names, and avoid diagnosis, medical advice, or invented checkup results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/elder-checkup-voice)
- [Beatra skill homepage](https://beatra.ai/skills/elder-checkup-voice)
- [Elder checkup voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown with labeled cue lists, JSON payload examples, shell commands, and generated MP3 file links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is 8 to 20 clips; paid clone and speech requests require separate confirmation and opaque client_request_id values.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
