## Description:

MoPNG API helps OpenClaw agents negotiate and run MoPNG Agent OpenAPI image generation and editing workflows, including text-to-image, image-to-image, background removal or replacement, outpainting, upscaling, and multi-step plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jkin8010](https://clawhub.ai/user/jkin8010)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use this skill to convert image generation or editing requests into a MoPNG Agent brief, review and revise the returned plan, approve execution, and deliver generated image links or text results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-approve paid remote image work when a returned plan is under the configured cost threshold.

Mitigation: Use manual brief, plan, approve, and status commands, or disable auto-approval with --no-auto-approve or MOPNG_AGENT_AUTO_APPROVE_COST_POINTS=0.

Risk: The release includes a broader legacy API client outside the advertised MoPNG Agent workflow.

Mitigation: Use scripts/mopng_agent.py for the documented agent workflow and invoke scripts/mopng_api.py only when explicitly intending to use the older direct API client.

Risk: The skill requires a MoPNG API key and submits authorized remote image jobs.

Mitigation: Keep MOPNG_API_KEY in private host configuration, avoid logging it, and send only user-approved HTTPS image URLs.

## Reference(s):

- [Server-resolved source repository](https://github.com/jkin8010/mopng-api)
- [ClawHub skill page](https://clawhub.ai/jkin8010/skills/mopng-api)
- [MoPNG Agent API endpoint](https://agent-api.mopng.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return remote result image URLs or text results from the MoPNG Agent service.]

## Skill Version(s):

0.1.8 (source: server release evidence; artifact pyproject.toml reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
