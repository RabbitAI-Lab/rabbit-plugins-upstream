## Description:

Guides agents through a five-domain workflow for composing avatar, outfit, motion, voiceover, background, and product elements into AI try-on, dance, runway, talking-avatar, pose videos, static assets, and reusable asset combinations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to plan and execute avatar outfit and motion media workflows, including collecting required inputs, generating or reusing six element assets, selecting a composition path, and producing short videos or static deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill works with sensitive face, voice, video, product, and brand assets.

Mitigation: Use only assets with clear rights and consent, and require disclosure or labeling for synthetic endorsements or lip-sync content.

Risk: The bundled depth scripts load external PyTorch .pth model weights.

Mitigation: Use model weights only from trusted pinned sources, verify their SHA-256 hashes, and avoid loading untrusted .pth files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/avatar-outfit-motion-video)
- [ClawHub publisher profile](https://clawhub.ai/user/wangjiaocheng)
- [Avatar Outfit Motion Catalog](references/avatar-outfit-motion-catalog.md)
- [Avatar Outfit Motion Requirements](references/avatar-outfit-motion-requirements.md)
- [Avatar Outfit Motion Exemplars](references/avatar-outfit-motion-exemplars.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional Python and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request or reference image, video, audio, model-weight, and generated media asset files.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
