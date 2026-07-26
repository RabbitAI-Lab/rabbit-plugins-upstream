## Description: <br>
A specialized skill for generating high-quality, consistent children's bilingual picture books using 'banana nano', with visual style, scene, age-driven content, learning-domain, and character-consistency guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate bilingual Chinese/English children's picture-book stories, learning points, and image prompts tailored by style, scene, age, page count, and character choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated stories and prompts may be saved locally under ./output/picture-books. <br>
Mitigation: Review generated files before sharing and avoid including sensitive personal information in prompts or story content. <br>
Risk: The artifact includes guidance to suppress or remove watermark and provenance marks. <br>
Mitigation: Use that guidance only when you have clear rights to the images and the image provider's terms allow it. <br>
Risk: The cleanup script can delete listed documentation files when run without dry-run mode. <br>
Mitigation: Run cleanup-duplicates.sh with --dry-run first and keep source control or backups before deleting files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/kart-io-picture-book-wizard) <br>
- [Skill README](artifact/README.md) <br>
- [English skill instructions](artifact/SKILL-en.md) <br>
- [Output format template](artifact/assets/templates/output-format.md) <br>
- [Reference guide](artifact/references/REFERENCE.md) <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with bilingual story text, pinyin, learning points, image prompts, and optional saved-file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save generated story files under ./output/picture-books when the file-output workflow is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
