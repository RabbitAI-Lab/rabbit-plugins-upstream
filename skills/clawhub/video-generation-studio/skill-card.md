## Description:

Plan and create short AI videos from a written shot, a supplied image, exact first and last frames, multimodal references, or existing footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, submit, monitor, and review short Beatra AI video and image generation tasks for ads, product stories, social clips, b-roll, transitions, reveals, and cinematic concepts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra connection uses a broad shared device token that can include wallet spending and non-video media scopes.

Mitigation: Install only after confirming those permissions are acceptable, review account and device revocation controls, and avoid uploading sensitive local media unless it is intended for Beatra processing.

Risk: Automatic package updates are enabled by default.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when automatic replacement is not acceptable.

Risk: Video and image generation can consume credits through paid asynchronous tasks.

Mitigation: Require the skill's admission card and user balance or top-up confirmation before paid calls, then report only returned terminal billing facts.

## Reference(s):

- [Skill package page](https://clawhub.ai/beatra-ai/skills/video-generation-studio)
- [Beatra skill homepage](https://beatra.ai/skills/video-generation-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Shot design](references/shot-design.md)
- [Image-assisted video](references/image-assisted-video.md)
- [Video recipes](references/video-recipes.md)
- [Review and iteration](references/review-and-iteration.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP call payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local media, call Beatra MCP tools, and return generated image or video artifact links through the agent.]

## Skill Version(s):

0.1.4 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
