## Description:

Generate lip-synced talking head videos from portrait images and audio using WaveSpeed AI's InfiniteTalk model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create talking avatar videos from a portrait image and speech audio. It supports optional face masks, prompt guidance, resolution selection, and repeatable seeds for WaveSpeed AI InfiniteTalk generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npm CLI and MCP setup can change behavior between installs or runs.

Mitigation: Pin reviewed versions of @wavespeed/cli and @wavespeed/mcp in controlled environments and inspect the live model schema before generation.

Risk: Portrait images, audio, mask images, and media URLs may be uploaded or sent to WaveSpeed for generation.

Mitigation: Use only approved user-provided media and avoid sensitive portraits or audio unless the user has confirmed they are comfortable sending them to WaveSpeed.

Risk: API keys could be exposed if pasted into chat or command transcripts.

Mitigation: Use wavespeed login or the WAVESPEED_API_KEY environment variable, and do not ask users to paste secrets into chat.

Risk: Video generation has usage costs and incorrect full-image masks can produce black outputs.

Mitigation: Quote pricing before long runs, start with lower resolution when appropriate, and use masks that cover only the face region to animate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-infinitetalk-avatar)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key login](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash command examples, parameter tables, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to call the WaveSpeed InfiniteTalk model and return generated video URLs or downloaded video files.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter says 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
