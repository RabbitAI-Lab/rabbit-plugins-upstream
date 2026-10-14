## Description:

Guides agents through FLUX image-generation and editing workflows by choosing the right variant and license path, writing scene prompts and edit instructions, preserving brand and reference consistency, and requiring human review before publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[social-media-skills](https://clawhub.ai/user/social-media-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and agents use this skill to plan commercial FLUX image workflows, write prompts and edit instructions, select model variants by rights and capability, and prepare on-brand image outputs for human review and WoopSocial publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected FLUX workflows may send prompts, brand details, and reference images to image-generation providers.

Mitigation: Use only approved providers for the data involved, avoid sensitive or unconsented reference images, and confirm provider terms before commercial use.

Risk: FLUX variant licensing can differ between hosted APIs, Apache-licensed weights, and self-hosted dev weights.

Mitigation: Verify the current rights for the exact variant and deployment path before use, especially for self-hosted commercial services.

Risk: Generated images can contain unauthorized likenesses, cloned trade dress, missing disclosures, stripped provenance, or incorrect rendered text.

Mitigation: Require human review before publishing, use consented or original references, preserve provenance metadata, apply required AI disclosures, and check all rendered text character by character.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/social-media-skills/skills/flux)
- [The reality of FLUX in 2026](artifact/references/flux-2026-reality.md)
- [Prompt patterns, decision tables & worked examples](artifact/references/prompt-patterns-and-templates.md)
- [Scope, distinctions & connections](artifact/references/scope-and-connections.md)
- [The PIXEL framework](artifact/references/the-pixel-framework.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, api calls]

**Output Format:** [Markdown guidance with scene prompts, edit instructions, variant and license decision notes, review gates, and optional connected API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human judgment for every generated or edited image; connected image-generation APIs and reference images may be used when available.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
