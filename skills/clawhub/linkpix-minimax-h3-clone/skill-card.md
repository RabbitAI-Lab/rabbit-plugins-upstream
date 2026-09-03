## Description:

This skill helps livestream and ecommerce teams use Qinghu AI, qhkit, and MiniMax H3 to analyze viral video links, rewrite scripts for a user's product, and generate emotionally matched product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, livestream operators, content creators, and agents use this skill to convert reference video links into rewritten product scripts and MiniMax H3 product-video generation requests. It supports workflows for Douyin, Xiaohongshu, WeChat Channels, TikTok, and similar short-video commerce channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request or configure a raw Qinghu API key.

Mitigation: Use a platform secret store or preconfigured environment variable, and do not paste API keys into chat.

Risk: The skill can install host-level tooling and run qhkit commands that submit paid video-generation jobs.

Mitigation: Run it in an isolated environment, review install commands before execution, estimate credits before generation, and require explicit user approval before submitting paid jobs.

Risk: External media is processed by Qinghu/qhkit services.

Mitigation: Use the skill only when external media processing is acceptable for the user's content and policy context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-clone)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with qhkit command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include video-analysis guidance, rewritten script text, command proposals, polling instructions, and generated media URLs when the external service completes successfully.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
