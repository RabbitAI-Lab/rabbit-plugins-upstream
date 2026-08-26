## Description:

Reconstructs user-supplied portraits and environment photos as Disco Elysium-inspired psychological paintings and concept art while preserving identity or place anchors and requiring suitability confirmation before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhilogic-oss](https://clawhub.ai/user/zhilogic-oss)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative workers use this skill to assess a supplied portrait or environment photo, confirm suitability, and transform it into one image-generation result with a Disco Elysium-inspired portrait or environmental concept-art treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided photos may be sent to the image-generation tool used by the agent.

Mitigation: Use photos the user owns or has permission to transform, and be especially careful with identifiable people.

Risk: The requested aesthetic could be mistaken for official affiliation or could drift toward protected game assets.

Mitigation: Keep the game name as an aesthetic reference only, and do not add game characters, UI, logos, dialogue boxes, title typography, screenshots, or official assets.

Risk: A transformation can lose the recognizable identity of a person or the essential anchors of a place.

Mitigation: Use the suitability gate, preserve identity topology or place anchors, and run the quality checklist before returning the result.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/zhilogic-oss/photo-to-disco-elysium)
- [ClawHub skill page](https://clawhub.ai/zhilogic-oss/skills/photo-to-disco-elysium)
- [README](README.md)
- [Visual Language](references/visual-language.md)
- [Transformation Contract](references/transformation-contract.md)
- [Portrait Art Direction](references/portrait-art-direction.md)
- [Environment Art Direction](references/environment-art-direction.md)
- [Prompt Compiler](references/prompt-compiler.md)
- [Quality Checklist](references/quality-checklist.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Image-generation prompts, Files]

**Output Format:** [Markdown guidance and image-generation/editing instructions, with one transformed image file returned by the agent when generation is confirmed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [First-turn suitability gate; one independent output image per source photo by default; internal analysis and prompts are withheld unless requested.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
