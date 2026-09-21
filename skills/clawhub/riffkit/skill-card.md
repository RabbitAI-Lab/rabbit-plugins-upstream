## Description:

Riffkit helps an agent turn one source video, TikTok link, analyzed template, or written creative direction into a short AI video or UGC-style ad with optional digital character, product placement, and language settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to plan, submit, monitor, and retrieve short AI video riffs or original ad videos through Riffkit after explicit user confirmation. It also guides authentication, product and media uploads, billing-aware error handling, captions, hashtags, and iteration advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat update path can replace local skill instructions from riffkit.ai after the version check.

Mitigation: Install only if the Riffkit update channel is trusted, or disable/manualize the heartbeat and review changed skill files before use.

Risk: The skill uses Riffkit API access and a device-flow session cookie.

Mitigation: Use the documented device authorization flow, treat vee_session as a credential, and avoid exposing it in chat, task fields, captions, product data, or logs.

Risk: Billable video generation and product or media uploads can be triggered after confirmation.

Mitigation: Require explicit submit confirmation, present billing or 402 shortfall information when applicable, and confirm the purpose of files before uploading user media.

## Reference(s):

- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill source](https://riffkit.ai/SKILL.md)
- [Riffkit heartbeat procedure](https://riffkit.ai/HEARTBEAT.md)
- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit publisher profile](https://clawhub.ai/user/riffkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown guidance with API paths, shell command examples, JSON request and response shapes, and final video delivery details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit submit confirmation before billable generation; finished outputs can include video download links, captions, hashtags, and strategy recap.]

## Skill Version(s):

1.7.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
