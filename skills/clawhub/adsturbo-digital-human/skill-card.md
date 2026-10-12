## Description:

Helps create talking-avatar videos from a script, a custom photo and voice sample, or a portrait paired with audio using AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to produce narrated talking-avatar videos, clone an authorized persona, or lip-sync a portrait to audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face or voice cloning without the subject's permission.

Mitigation: Use only portraits and recordings you own or are explicitly authorized to use; obtain consent before cloning another person's likeness or voice.

Risk: Portraits and voice samples require publicly accessible media URLs, and generated-persona data is sent to AdsTurbo.

Mitigation: Upload only media you are comfortable sharing with AdsTurbo and making accessible by URL; avoid sensitive personal material.

Risk: Unpinned software dependencies may change after installation.

Mitigation: Consider pinning dependencies before running the skill in a controlled environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/adsturbo/skills/adsturbo-digital-human)
- [AdsTurbo API access](https://adsturbo.ai/iris/api)
- [Digital human usage reference](artifact/references/digital_human.md)
- [Media upload reference](artifact/references/upload.md)
- [Task status reference](artifact/references/work.md)

## Skill Output:

**Output Type(s):** [Text, Links, Guidance]

**Output Format:** [Plain text with links to generated video or audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some generation tasks complete asynchronously; API access uses credits.]

## Skill Version(s):

1.2.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
