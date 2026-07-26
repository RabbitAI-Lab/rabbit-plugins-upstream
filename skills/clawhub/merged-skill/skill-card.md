## Description: <br>
Generate professional social cards and magazine-style posters using Editorial and Swiss visual systems for Xiaohongshu, WeChat covers, magazine posters, social cards, carousel images, and other high-quality visual content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gf1023456](https://clawhub.ai/user/gf1023456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent users use this skill to turn articles, product notes, screenshots, photos, or copy into social-ready visual assets such as Xiaohongshu carousels, WeChat cover pairs, and magazine-style posters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can be installed persistently and selected for future visual-design requests. <br>
Mitigation: Review install and update commands before enabling the skill, and keep its use scoped to intended visual-generation workflows. <br>
Risk: Image sourcing and rendered pages may make outbound requests for web images, fonts, maps, or other embedded assets. <br>
Mitigation: Approve web searches or downloads only for non-sensitive content, review source records, and render only trusted HTML. <br>
Risk: Generated social visuals can contain layout, overflow, attribution, or source-use issues if outputs are accepted without review. <br>
Mitigation: Inspect rendered PNGs, review generated source notes, and run the included validation script when a stricter layout check is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gf1023456/skills/merged-skill) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.en.md](artifact/README.en.md) <br>
- [Platform specs](artifact/references/platform-specs.md) <br>
- [Layout recipes](artifact/references/layout-recipes.md) <br>
- [Theme presets](artifact/references/theme-presets.md) <br>
- [Production workflow](artifact/references/production-workflow.md) <br>
- [QA checklist](artifact/references/qa-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with HTML/CSS code and shell commands; rendered output is PNG files from single-file HTML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate task-local HTML, source-tracking notes, and optional Playwright validation reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
