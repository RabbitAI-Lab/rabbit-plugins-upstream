## Description:

LinkFox e-commerce IP and compliance toolkit that helps agents check product images and listing text for copyright, trademark, patent, policy, and patent-information risks using Ruiguan and PatSnap/Zhihuiya services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, compliance reviewers, and agents use this skill before product launch to inspect images and listing text for potential copyright, trademark, design-patent, utility-patent, and image-policy issues, and to retrieve patent data, translations, images, legal status, family, citation, and PDF information. The outputs support risk review and research, but the skill does not provide legal advice or infringement conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API keys, product images or listing text, patent queries, and onboarding data to LinkFox-controlled or configurable web endpoints.

Mitigation: Install and run it only when LinkFox is an approved data recipient, use a scoped API key, and avoid custom endpoint environment variables unless the destination is controlled and trusted.

Risk: Local image uploads create public URLs for product images.

Mitigation: Upload only images that are acceptable to expose through a temporary public URL, and avoid sensitive or confidential imagery unless the disclosure path is approved.

Risk: Full API responses may be cached or saved outside the project directory if the preferred output path is unavailable.

Mitigation: Review generated `linkfox/` data and cache files after use, avoid passing unnecessary sensitive fields, and clean stored responses according to the workspace data-retention policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ecommerce-compliance-detection)
- [Ruiguan Copyright Detection](artifact/references/linkfox-ruiguan-copyright-detection.md)
- [Ruiguan Design Patent Detection](artifact/references/linkfox-ruiguan-detection-patent-design.md)
- [Ruiguan Image Policy Compliance](artifact/references/linkfox-ruiguan-gun-parts-search.md)
- [Ruiguan Text Trademark Detection](artifact/references/linkfox-ruiguan-text-trademark-detection.md)
- [Ruiguan Graphic Trademark Detection](artifact/references/linkfox-ruiguan-trademark-graphic-detection.md)
- [Ruiguan Utility Patent Detection](artifact/references/linkfox-ruiguan-utility-patent-detection.md)
- [Zhihuiya Patent Image Search](artifact/references/linkfox-zhihuiya-patent-image-search.md)
- [Zhihuiya Utility Patent Image Search](artifact/references/linkfox-zhihuiya-utility-patent-image-search.md)
- [Zhihuiya Simple Bibliography](artifact/references/linkfox-zhihuiya-simple-bibliography.md)
- [Zhihuiya Patent Bibliography](artifact/references/linkfox-zhihuiya-bibliography.md)
- [Zhihuiya Abstract Translation](artifact/references/linkfox-zhihuiya-abstract-data-translated.md)
- [Zhihuiya Claims Data](artifact/references/linkfox-zhihuiya-claim-data.md)
- [Zhihuiya Claims Translation](artifact/references/linkfox-zhihuiya-claim-data-translated.md)
- [Zhihuiya Description Data](artifact/references/linkfox-zhihuiya-description-data.md)
- [Zhihuiya Description Translation](artifact/references/linkfox-zhihuiya-description-data-translated.md)
- [Zhihuiya Abstract Image](artifact/references/linkfox-zhihuiya-abstract-image.md)
- [Zhihuiya Fulltext Image](artifact/references/linkfox-zhihuiya-fulltext-image.md)
- [Zhihuiya Legal Status](artifact/references/linkfox-zhihuiya-legal-status.md)
- [Zhihuiya Patent Family](artifact/references/linkfox-zhihuiya-patent-family.md)
- [Zhihuiya Patent Cited](artifact/references/linkfox-zhihuiya-patent-cited.md)
- [Zhihuiya Patent Forward Citation](artifact/references/linkfox-zhihuiya-patent-forward-citation.md)
- [Zhihuiya Patent PDF Data](artifact/references/linkfox-zhihuiya-pdf-data.md)
- [Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, summaries, saved result files, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; image workflows require public image URLs or temporary uploaded public URLs; large API responses may be summarized while full JSON is saved locally.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
