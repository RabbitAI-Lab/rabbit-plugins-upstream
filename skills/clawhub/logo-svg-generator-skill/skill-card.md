## Description: <br>
Generate multi-size SVG logos from natural-language product briefs, following Simple Icons design rules with an iterative generate, visual-check, and optimize loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and product teams use this skill to turn product briefs into Simple-Icons-style SVG logo assets, PNG previews, favicon files, and review summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brief details and generated logo assets may be saved locally and may be shared with a vision-capable LLM during review. <br>
Mitigation: Use an approved workspace and model for confidential branding, or choose the explicit structural-only path and complete human visual review before release. <br>
Risk: Generated logos may still be off-brand, hard to read at small sizes, or unsuitable for production use despite automated checks. <br>
Mitigation: Review the final SVG, previews, and review summary with a human brand owner before publishing or relying on the assets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/samonysh/skills/logo-svg-generator-skill) <br>
- [Source Repository](https://github.com/samonysh/logo-svg-generator-skill) <br>
- [Simple Icons](https://simpleicons.org/) <br>
- [Simple Icons Contributing Guide](https://github.com/simple-icons/simple-icons/blob/develop/CONTRIBUTING.md) <br>
- [Simple Icons Slug Rules](https://github.com/simple-icons/simple-icons/blob/develop/slugs.md) <br>
- [Design Rules](references/design-rules.md) <br>
- [Motif Patterns](references/motif-patterns.md) <br>
- [Sample Icons](references/sample-icons.md) <br>
- [Visual Review Prompt](assets/templates/visual-review-prompt.md) <br>
- [Concept Brief Template](assets/templates/concept-brief-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Markdown, Configuration, Guidance] <br>
**Output Format:** [SVG, PNG, ICO, JSON, and Markdown files with concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a 24x24 master SVG, multi-size monochrome and color variants, preview assets, brand metadata, and review notes when available.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
