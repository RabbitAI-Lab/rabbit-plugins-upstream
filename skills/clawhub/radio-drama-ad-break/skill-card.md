## Description:

Turn written radio-drama ad-break lines into one spoken bumper clip per labeled slot. This radio-drama bumper studio records each pre-roll read, post-roll read, and sponsor bumper from the copy the producer already wrote, then delivers 8 to 20 bumper audio files. Use it for radio drama ad-break voiceovers that keep one bumper on each clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External producers and audio creators use this skill to turn prewritten radio-drama ad-break, sponsor, and bumper copy into labeled spoken clips. It helps plan the slot list, confirm paid voice clone or speech work, submit Beatra generation requests, and recover task or billing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a shared Beatra authorization that can spend credits and access broad Beatra account capabilities.

Mitigation: Install and use it only on machines where the user trusts Beatra account and credit controls; review each paid clone or speech card before submission and revoke the device from the Beatra Console when no longer needed.

Risk: The bundled client can invoke exposed Beatra MCP tools, so an incorrect or unintended call could start paid or account-affecting work.

Mitigation: Use the skill's confirmation flow, preserve opaque request identities for paid work, and submit only the intended Beatra operation with the exact approved arguments.

Risk: The package silently checks for and applies verified updates by default.

Mitigation: Disable automatic checks with `python3 scripts/mcp_client.py update --auto off` when local change control requires manual review; otherwise rely on the documented checksum, manifest, and fixed-source verification before replacement.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/radio-drama-ad-break)
- [Beatra Skill Homepage](https://beatra.ai/skills/radio-drama-ad-break)
- [Radio-drama bumper workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance, Audio files]

**Output Format:** [Markdown with inline JSON and shell commands, plus generated MP3 bumper audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one clip per labeled bumper slot, typically 8 to 20 clips, using live Beatra model, billing, task, and wallet responses.]

## Skill Version(s):

0.1.3 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
