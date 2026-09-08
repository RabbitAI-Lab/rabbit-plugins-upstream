## Description:

Generates lip-synced talking-avatar videos from a portrait image and audio using WaveSpeed AI's InfiniteTalk model, with optional face masks and prompt guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to animate a portrait or selected face from an audio track, producing a talking-avatar video through WaveSpeed AI's InfiniteTalk model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing WaveSpeed npm packages can introduce package supply-chain risk.

Mitigation: Install only if the WaveSpeed packages and service are trusted; prefer a non-privileged shell, and consider pinning package versions or using a project-local install.

Risk: WaveSpeed API credentials can be exposed if pasted into chat or handled casually.

Mitigation: Use the documented login flow or a local environment variable, and do not ask users to paste API keys into the conversation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-infinitetalk-avatar)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key login](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and generated output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a WaveSpeed prediction id and video output URL; generated media duration follows the source audio up to 10 minutes.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
