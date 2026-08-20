## Description:

Avatar Outfit Motion Video guides agents through a three-step avatar, outfit, and motion pipeline for AI try-on, dance, catwalk, lip-sync, digital-human, and pose videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and media operators use this skill to plan and execute avatar-outfit-motion video workflows, including tri-view identity assets, depth-video motion extraction, path selection, video synthesis, and quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles faces, voices, videos, and possible cloud-upload workflows without clear consent and privacy safeguards.

Mitigation: Use only media the operator owns or is authorized to use, review provider retention and deletion terms before uploading assets, and prefer local processing for sensitive material.

Risk: Generated avatar, outfit, motion, or lip-sync outputs can misrepresent identity, consent, or likeness rights when source media includes identifiable people.

Mitigation: Confirm rights and consent before processing identifiable faces, voices, or videos, and run the documented quality and compliance review before delivery.

Risk: Cloud connector path selection can expose portraits, audio, or video to external services.

Mitigation: Document the selected path and resource basis, avoid cloud upload for sensitive assets unless terms are acceptable, and use local or degraded paths when privacy is the priority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/avatar-outfit-motion-video)
- [Avatar Outfit Motion Catalog](references/avatar-outfit-motion-catalog.md)
- [Avatar Outfit Motion Requirements](references/avatar-outfit-motion-requirements.md)
- [Avatar Outfit Motion Exemplars](references/avatar-outfit-motion-exemplars.md)
- [DINO Vision Transformer reference](https://github.com/facebookresearch/dino/blob/main/vision_transformer.py)
- [PyTorch Image Models Vision Transformer reference](https://github.com/rwightman/pytorch-image-models/tree/master/timm/models/vision_transformer.py)
- [PyTorch Image Models DropPath reference](https://github.com/rwightman/pytorch-image-models/tree/master/timm/layers/drop.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with tables, prompts, shell commands, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of PNG depth images, MP4 depth videos, and final MP4 videos through local scripts or external video-generation paths.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
