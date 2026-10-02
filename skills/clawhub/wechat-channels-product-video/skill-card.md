## Description:

Creates a vertical WeChat Channels product showcase video, title, and publishing copy from a real product photo and confirmed product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and content creators use this skill to turn an authorized product photo and verified product facts into a short vertical WeChat Channels showcase video and ready-to-use publishing copy. The user reviews and publishes the result separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to Beatra.

Mitigation: Send only photos you may share and product details you are comfortable disclosing.

Risk: The shared Beatra device token grants access beyond this video workflow.

Mitigation: Review the access before connecting and revoke the Beatra device in the Beatra Console when no longer needed.

Risk: Automatic package updates are enabled by default and may change installed behavior without separate approval.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you prefer to review updates first.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/wechat-channels-product-video)
- [Publisher skill page](https://beatra.ai/skills/wechat-channels-product-video)
- [Video channel planning](references/video-channel-planning.md)
- [Video workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown with a generated video reference, title, and publishing copy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requires approval and Beatra credits; the user publishes the video separately.]

## Skill Version(s):

0.2.2 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
