## Description:

Turns attributed game or murder-mystery scripts into ordered, character-labeled voice clips using a consistent voice for each role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers and tabletop creators use this skill to cast characters, synthesize scripted dialogue, and deliver line-numbered voice clips ready for import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra token can authorize other media-generation scopes and wallet spending beyond voice packs.

Mitigation: Review the requested account access before approving it, and confirm the cast and current credit estimate before paid generation.

Risk: Automatic updates can replace local skill code without a separate prompt.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when code changes require review.

Risk: The skill stores local account state in ~/.beatra and uninstalling the last Beatra skill may revoke the shared connection.

Mitigation: Use the documented uninstall flow and check whether other Beatra skills still rely on the connection.

Risk: Voice cloning can reproduce a speaker's voice without their permission.

Mitigation: Require explicit speaker authorization before uploading a sample or requesting a clone.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/game-script-voice-pack)
- [Game voice-pack workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation and authentication](references/installation-and-auth.md)

## Skill Output:

**Output Type(s):** [Audio files, Text, Markdown]

**Output Format:** [Numbered MP3 clips and a character-labeled line ledger with artifact links and billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One stable voice per role; clip order follows the script.]

## Skill Version(s):

0.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
