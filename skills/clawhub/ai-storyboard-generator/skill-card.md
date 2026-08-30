## Description:

Turn a script, scene, or ad brief into a structured AI storyboard plan with a practical shot list and one to four storyboard key-frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, producers, designers, and developers use this skill to turn scripts, scene outlines, and advertising briefs into reviewable storyboard shot lists and a small set of approved key-frame images before production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared full-scope Beatra device authorization and local ~/.beatra state.

Mitigation: Install only when that authorization posture is acceptable, keep the credential file private, and use the documented uninstall or Beatra Console revocation flow when disconnecting.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates with the documented update command when review-before-change behavior is required.

Risk: Key-frame generation is paid work and duplicate submissions can create duplicate tasks or charges.

Mitigation: Use the required approval step, submit each approved shot once with a stable client_request_id, and recover uncertain results by polling or retrying only the identical request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-storyboard-generator)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-storyboard-generator)
- [Storyboard planning and key frames](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown shot lists, frame prompts, approval plans, shell commands, and returned artifact details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include one to four generated storyboard key-frame artifacts after user approval and paid Beatra image tasks.]

## Skill Version(s):

0.1.6 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
