## Description:

Turn a murder-mystery or indie-game script into a labeled multi-character voice pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, game teams, and tabletop producers use this skill to convert attributed game or mystery scripts into ordered, character-labeled voice clips while keeping one voice assignment per role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill can use Beatra account capabilities beyond voice generation.

Mitigation: Review the requested account access before installation and run paid or account-affecting operations only after the user confirms the specific task and estimate.

Risk: The security guidance says the skill stores a shared bearer credential locally.

Mitigation: Keep the Beatra credential files private to the local user, avoid exposing tokens in chat or logs, and use the uninstall or disconnect guidance when access is no longer needed.

Risk: The security guidance says package files may be replaced automatically unless automatic updates are disabled.

Mitigation: Use the documented update controls to disable automatic checks when a locked package version is required, and review updates before re-enabling automatic replacement.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/game-script-voice-pack)
- [Beatra Skill Homepage](https://beatra.ai/skills/game-script-voice-pack)
- [Game voice-pack workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown summary with labeled audio file artifacts or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes character IDs, line IDs, clip ordering, duration, MIME type, resolved model, and reported net credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
