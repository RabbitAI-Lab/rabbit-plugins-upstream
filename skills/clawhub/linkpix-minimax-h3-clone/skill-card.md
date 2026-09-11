## Description:

This skill helps livestream and social commerce teams use Qinghu AI and qhkit to analyze a viral video, rewrite its structure for a user's product, and generate a MiniMax H3-style product video with matching pacing, voice, emotion, and optional multilingual delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External livestream, creator, and social commerce teams use this skill to turn a reference short-video link into a rewritten product script and a MiniMax H3-style generated product video through qhkit. It is intended for viral product-video adaptation, multilingual voiceover replication, and batch social content production while avoiding direct reuse of original scripts or media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for qhkit credentials and security evidence warns against pasting API keys into chat.

Mitigation: Configure credentials through a local secret mechanism or QHKIT_TOKEN, and avoid sharing raw API keys in conversation.

Risk: The skill directs agents to install mutable global or latest dependencies.

Mitigation: Prefer pinned, local, reviewed qhkit dependencies where possible, and review install commands before execution.

Risk: Viral video adaptation can copy protected scripts, media, or likeness too closely.

Mitigation: Use the reference only for structure and creative direction, rewrite the script for the user's product, and confirm the rewritten version before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include original and rewritten script comparisons, generation parameters, task IDs, polling guidance, media URLs, and credit estimates.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
