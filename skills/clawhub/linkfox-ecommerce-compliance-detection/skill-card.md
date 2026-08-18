## Description:

LinkFox E-commerce Compliance Detection helps agents check e-commerce product images and text for copyright, trademark, design patent, utility patent, prohibited-product, and patent-data risks using LinkFox tool endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, compliance reviewers, and developers use this skill before listing products to investigate IP and product-policy risk signals, retrieve patent information, and prepare evidence summaries for human review. It reports similarity, rights-owner, legal-status, TRO, and patent-family data but does not provide legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials and compliance-check inputs may be sent to endpoints selected through environment variables.

Mitigation: Set LinkFox endpoint environment variables only to trusted LinkFox services and avoid running the skill in untrusted shells or shared workspaces.

Risk: Full compliance results may be written to local linkfox output or cache directories after a run.

Mitigation: Review generated result files for sensitive product, patent, or listing data and clean the linkfox output/cache directories when retention is not required.

Risk: The skill reports IP and compliance risk signals that can be mistaken for legal conclusions.

Mitigation: Treat results as supporting evidence for human review and consult qualified counsel before making infringement, FTO, listing, or litigation decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ecommerce-compliance-detection)
- [Skill overview](artifact/SKILL.md)
- [Onboarding](artifact/references/onboarding.md)
- [Ruiguan copyright detection](artifact/references/linkfox-ruiguan-copyright-detection.md)
- [Ruiguan graphic trademark detection](artifact/references/linkfox-ruiguan-trademark-graphic-detection.md)
- [Ruiguan text trademark detection](artifact/references/linkfox-ruiguan-text-trademark-detection.md)
- [Ruiguan design patent detection](artifact/references/linkfox-ruiguan-detection-patent-design.md)
- [Ruiguan utility patent detection](artifact/references/linkfox-ruiguan-utility-patent-detection.md)
- [Ruiguan prohibited-product image search](artifact/references/linkfox-ruiguan-gun-parts-search.md)
- [Zhihuiya patent image search](artifact/references/linkfox-zhihuiya-patent-image-search.md)
- [Zhihuiya utility patent image search](artifact/references/linkfox-zhihuiya-utility-patent-image-search.md)
- [Zhihuiya patent bibliography](artifact/references/linkfox-zhihuiya-bibliography.md)
- [Zhihuiya simple bibliography](artifact/references/linkfox-zhihuiya-simple-bibliography.md)
- [Zhihuiya claims and translations](artifact/references/linkfox-zhihuiya-claim-data.md)
- [Zhihuiya legal status](artifact/references/linkfox-zhihuiya-legal-status.md)
- [Zhihuiya patent family](artifact/references/linkfox-zhihuiya-patent-family.md)
- [Zhihuiya citations](artifact/references/linkfox-zhihuiya-patent-cited.md)
- [Zhihuiya PDF data](artifact/references/linkfox-zhihuiya-pdf-data.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON result summaries, shell commands, and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include summarized API responses and references to locally saved JSON result files.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
