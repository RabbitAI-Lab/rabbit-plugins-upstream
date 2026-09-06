## Description:

Animates characters from images using driving videos with WaveSpeed AI's Wan 2.2 Animate model, supporting animate and replace modes with outputs up to 120 seconds at 480p or 720p.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operators use this skill to generate guidance and commands for animating a still character image from a driving video or replacing a video subject with an image character through WaveSpeed AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, prompts, and generated outputs may be uploaded to and processed by WaveSpeed AI.

Mitigation: Use only media that the user has permission to process, review the provider's data terms, and avoid confidential, biometric, regulated, or proprietary media unless approved.

Risk: The skill relies on third-party npm CLI or MCP tooling for execution.

Mitigation: Install the tools only in environments where third-party CLI code is acceptable, avoid running them as root, and keep authentication scoped to the intended WaveSpeed account.

Risk: API credentials could be exposed if copied into chat or commands are mishandled.

Mitigation: Use `wavespeed login` or `WAVESPEED_API_KEY` in the environment, and do not ask users to paste API keys into chat.

Risk: Untrusted or unintended media URLs could be submitted to the service.

Mitigation: Pass only user-provided media URLs or outputs from previous trusted runs, and keep model inputs limited to documented parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-wan-22-animate)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, MCP tool guidance, model parameter choices, pricing notes, and output URL handling.]

## Skill Version(s):

2.0.1 (source: server release evidence; artifact frontmatter reports 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
