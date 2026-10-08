## Description:

Guides creation of a narrated talking-avatar video from one authorized portrait and a short script or approved speech recording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to make single-presenter explainers, training clips, announcements, and product messages from an authorized portrait and narration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared full-scope Beatra device token can authorize paid, wallet-capable operations across Beatra skills.

Mitigation: Review the requested paid actions and charges before approval; keep the device credential private.

Risk: Portraits and voice recordings are processed by an external service, and unauthorized likeness or voice use can harm people.

Mitigation: Use only portraits, scripts, and voices you have rights to use; confirm authorization before generating or uploading media.

Risk: Silent automatic package updates can change installed skill behavior without a separate confirmation.

Mitigation: Review the skill before installation and consider disabling automatic updates with `python3 scripts/mcp_client.py update --auto off`.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/talking-avatar-video)
- [Beatra skill page](https://beatra.ai/skills/talking-avatar-video)
- [Narration-first presenter workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown with commands and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports accessible audio and video results, review observations, and actual charges when available.]

## Skill Version(s):

0.2.4 (source: ClawHub release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
