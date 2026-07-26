## Description: <br>
A color utility skill for color format conversion, contrast checks, palette recommendations, and local HTML preview generation for UI design and accessibility work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, frontend developers, and accessibility reviewers use this skill to convert color values, evaluate contrast, generate palette ideas, and produce local preview pages for visual inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Preview generation can write local HTML files and may overwrite an unintended file if the output path is ambiguous. <br>
Mitigation: Use explicit output paths for preview generation and review generated HTML before opening, sharing, or committing it. <br>
Risk: The skill may activate on general color-space mentions, and palette recommendations may require human judgment for brand or accessibility fit. <br>
Mitigation: Invoke it for explicit color tasks and verify final palettes, contrast choices, and accessibility decisions before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/color-toolkit-turn) <br>
- [Output examples](references/examples.md) <br>
- [FAQ](references/faq.md) <br>
- [Permissions](references/permissions.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown responses, JSON snippets, and optional local HTML preview files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Python standard-library color utilities and may write preview HTML files when requested.] <br>

## Skill Version(s): <br>
3.4.1 (source: server release metadata; artifact frontmatter and changelog list 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
