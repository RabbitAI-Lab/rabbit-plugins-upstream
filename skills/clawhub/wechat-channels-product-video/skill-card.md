## Description:

Create a vertical WeChat Channels product-display video from a real product photo and confirmed product information. Shape a clear product opening, one detail or use moment, and a clean ending, then prepare the finished product video with a title and publishing copy for WeChat Channels product content, including a new-product showcase video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to turn an inspectable product photo and user-confirmed product facts into a vertical WeChat Channels product showcase video plan, generated video result, title, and publishing copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad persistent Beatra account token stored in ~/.beatra/credentials.json.

Mitigation: Review before installing, use only if connecting a Beatra account is acceptable, keep the credential local, and revoke the connection when it is no longer needed.

Risk: The skill uploads selected product media to Beatra for generation.

Mitigation: Use only product media that may be shared with Beatra and avoid confidential or sensitive product images unless that upload is acceptable.

Risk: Executable package code silently self-updates by default.

Mitigation: Review before installing and disable automatic updates with python3 scripts/mcp_client.py update --auto off when reviewed code must remain fixed.

Risk: Installation metadata such as package, platform, and hostname information may be sent.

Mitigation: Install only when that metadata sharing is acceptable for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-channels-product-video)
- [WeChat Channels product-display video workflow](artifact/references/workflow.md)
- [Video Channels product-display planning](artifact/references/video-channel-planning.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with command examples, JSON payload sketches, publishing copy, and returned media artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, artifact URLs or IDs, resolved model details, dimensions, duration, usage, billing facts, and focused revision guidance when a paid task completes.]

## Skill Version(s):

0.1.8 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
