## Description:

Riffkit helps agents turn a TikTok link, uploaded video, analyzed template, or written creative direction into short AI riff videos or UGC-style ad creative with optional digital characters, product placement, and language settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riffkit](https://clawhub.ai/user/riffkit)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use Riffkit to prepare, submit, monitor, and deliver short-form AI video generation jobs from a source video, analyzed template, or written creative direction. The skill guides source selection, optional character and product placement settings, explicit pre-submit consent, progress monitoring, and delivery of video links, captions, hashtags, and strategy recaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heartbeat workflow can replace installed skill instructions from a remote URL without verification or approval.

Mitigation: Disable the heartbeat or change it to manual review unless updates are signed and verified; review and scan any new skill version before deployment.

Risk: The skill uses a Riffkit account session and can upload source videos or product media to Riffkit APIs.

Mitigation: Install only where users are comfortable connecting a Riffkit account, sending media to the service, and letting an agent call Riffkit APIs on their behalf.

Risk: Video generation is a paid action and retries may charge again.

Mitigation: Require explicit user confirmation before submit or retry, and surface insufficient-credit responses without silent retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit)
- [Riffkit homepage](https://riffkit.ai)
- [Riffkit skill source](https://riffkit.ai/SKILL.md)
- [Riffkit heartbeat source](https://riffkit.ai/HEARTBEAT.md)
- [Riffkit publisher profile](https://clawhub.ai/user/riffkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request parameters, shell command snippets, and generated video delivery details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before paid generation; finished outputs include download links, captions, hashtags, and strategy recaps.]

## Skill Version(s):

1.5.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
