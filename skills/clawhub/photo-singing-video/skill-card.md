## Description:

Guides an agent to turn one portrait and a short singing-audio excerpt into a singing video, then review the result for facial motion, identity, and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill to make a portrait sing a supplied song excerpt for greetings, character clips, or promotions, and to review the resulting video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device authorization grants broader account access than this photo-singing task needs.

Mitigation: Review the authorization scope before installing and only connect an account you are comfortable sharing with the client.

Risk: Automatic updates can replace local client code without a separate confirmation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you prefer to review updates first.

Risk: Video generation may incur credits and additional submissions may create new charges.

Mitigation: Check the current admission card and credit estimate before approving paid generation; recover uncertain submissions rather than starting a new one.

## Reference(s):

- [Photo Singing Video on ClawHub](https://clawhub.ai/beatra-ai/skills/photo-singing-video)
- [beatra-ai publisher profile](https://clawhub.ai/user/beatra-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with video artifact links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the returned task status, video details, and review observations when available.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
