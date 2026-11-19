## Description:

Routes image creation and editing requests across configured image services, and supports video generation through Jimeng and Grok.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ekko237](https://clawhub.ai/user/ekko237)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use the skill to generate or edit images and create videos through services they have configured, including reference-guided and batch jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review marks this release suspicious with medium confidence because some referenced scripts could not be fully interpreted; it lists no specific risk findings.

Mitigation: Review the referenced scripts before installation, as the server guidance recommends.

Risk: Prompts and selected reference images are sent to the external service used for a job.

Mitigation: Use only providers approved for the content, and do not send sensitive material unless the provider may receive it.

Risk: The optional pay-per-image service can charge for generated attempts even when an image is later discarded, and its spend caps are estimates.

Mitigation: Keep the paid line disabled unless requested, set budgets deliberately, and confirm estimated costs before paid generation.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/Ekko237/imagegen-swarm)
- [Setup and configuration](artifact/SETUP.md)
- [Codex engine details](artifact/references/codex.md)
- [Lovart engine details](artifact/references/lovart.md)
- [Muse approval scope](artifact/references/muse.md)

## Skill Output:

**Output Type(s):** [Image files, Video files, JSON status and result data]

**Output Format:** [PNG images, MP4 videos, and JSON status records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, aspect ratios, and batches; available engines, quotas, and optional spend limits affect results.]

## Skill Version(s):

1.4.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
