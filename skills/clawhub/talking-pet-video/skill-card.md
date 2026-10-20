## Description:

Turns a clear pet photo and approved speech or a short message into a talking-pet video, with checks for pet identity, speech clarity, and mouth synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and creators use this skill to turn a pet photo and approved audio or a short script into a shareable greeting, reaction, story, or dialogue clip through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants a shared full-scope Beatra device token and authority for paid generation, including access beyond talking-pet videos.

Mitigation: Review approval-page scopes and charges before connecting or submitting paid work; avoid accounts where unrelated Beatra access would be unacceptable.

Risk: The package installs newer releases silently by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you need to review releases before installation.

## Reference(s):

- [Talking-pet workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video artifact links]

**Output Format:** [Markdown with commands and a video result link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video requires Beatra access and user approval for paid stages.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
