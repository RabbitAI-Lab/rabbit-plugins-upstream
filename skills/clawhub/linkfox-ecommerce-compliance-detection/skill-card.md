## Description: <br>
Linkfox 电商合规检测 helps agents run e-commerce intellectual property compliance checks, patent lookups, and image-based patent searches using LinkFox Ruiguan and Zhihuiya tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to select and run LinkFox e-commerce IP compliance checks for copyright, trademark, design patent, utility patent, image policy, and patent data workflows. It is intended to surface structured risk indicators and patent records, not to provide legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send credentials and task data to an environment-selected LinkFox gateway. <br>
Mitigation: Use it only with a trusted HTTPS LINKFOX_TOOL_GATEWAY and scoped credentials for this service. <br>
Risk: API responses may be written outside the current project when the workspace is not writable. <br>
Mitigation: Run the skill in a controlled workspace and review generated linkfox session data paths before sharing or retaining outputs. <br>
Risk: The artifact includes a fallback path that may direct users to install a remote ZIP for onboarding. <br>
Mitigation: Avoid remote ZIP install fallback unless the package source is independently trusted and verified. <br>


## Reference(s): <br>
- [linkfox-ruiguan-copyright-detection.md](artifact/references/linkfox-ruiguan-copyright-detection.md) <br>
- [linkfox-ruiguan-detection-patent-design.md](artifact/references/linkfox-ruiguan-detection-patent-design.md) <br>
- [linkfox-ruiguan-gun-parts-search.md](artifact/references/linkfox-ruiguan-gun-parts-search.md) <br>
- [linkfox-ruiguan-text-trademark-detection.md](artifact/references/linkfox-ruiguan-text-trademark-detection.md) <br>
- [linkfox-ruiguan-trademark-graphic-detection.md](artifact/references/linkfox-ruiguan-trademark-graphic-detection.md) <br>
- [linkfox-ruiguan-utility-patent-detection.md](artifact/references/linkfox-ruiguan-utility-patent-detection.md) <br>
- [linkfox-zhihuiya-abstract-data-translated.md](artifact/references/linkfox-zhihuiya-abstract-data-translated.md) <br>
- [linkfox-zhihuiya-abstract-image.md](artifact/references/linkfox-zhihuiya-abstract-image.md) <br>
- [linkfox-zhihuiya-bibliography.md](artifact/references/linkfox-zhihuiya-bibliography.md) <br>
- [linkfox-zhihuiya-claim-data-translated.md](artifact/references/linkfox-zhihuiya-claim-data-translated.md) <br>
- [linkfox-zhihuiya-claim-data.md](artifact/references/linkfox-zhihuiya-claim-data.md) <br>
- [linkfox-zhihuiya-description-data-translated.md](artifact/references/linkfox-zhihuiya-description-data-translated.md) <br>
- [linkfox-zhihuiya-description-data.md](artifact/references/linkfox-zhihuiya-description-data.md) <br>
- [linkfox-zhihuiya-fulltext-image.md](artifact/references/linkfox-zhihuiya-fulltext-image.md) <br>
- [linkfox-zhihuiya-legal-status.md](artifact/references/linkfox-zhihuiya-legal-status.md) <br>
- [linkfox-zhihuiya-patent-cited.md](artifact/references/linkfox-zhihuiya-patent-cited.md) <br>
- [linkfox-zhihuiya-patent-family.md](artifact/references/linkfox-zhihuiya-patent-family.md) <br>
- [linkfox-zhihuiya-patent-forward-citation.md](artifact/references/linkfox-zhihuiya-patent-forward-citation.md) <br>
- [linkfox-zhihuiya-patent-image-search.md](artifact/references/linkfox-zhihuiya-patent-image-search.md) <br>
- [linkfox-zhihuiya-pdf-data.md](artifact/references/linkfox-zhihuiya-pdf-data.md) <br>
- [linkfox-zhihuiya-simple-bibliography.md](artifact/references/linkfox-zhihuiya-simple-bibliography.md) <br>
- [linkfox-zhihuiya-utility-patent-image-search.md](artifact/references/linkfox-zhihuiya-utility-patent-image-search.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may summarize large responses and write full JSON responses under a linkfox session data directory.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
