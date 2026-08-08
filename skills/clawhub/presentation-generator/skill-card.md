## Description: <br>
Generate polished slide decks as self-contained HTML and editable PowerPoint from notes, using structured deck JSON, presentation themes, schema layouts, and craft gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[isatimur](https://clawhub.ai/user/isatimur) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, founders, product teams, and sales or marketing teams use this skill to turn briefs, notes, Markdown, or PowerPoint inputs into polished presentation decks for pitches, investor updates, keynotes, product launches, and sales demos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential presentation content may be accidentally published through optional Vercel sharing. <br>
Mitigation: Deploy only decks that have been approved for external visibility, prefer preview deployments by default, and avoid deploying whole directories that may contain secrets or unrelated files. <br>
Risk: PDF export uses Node/npm tooling and Playwright/Chromium, which may fetch or render deck assets. <br>
Mitigation: Run export tooling in an environment approved for the deck content and keep the built-in route guard and JavaScript-disabled export path in place. <br>
Risk: Generated decks can contain incorrect, misleading, or off-brand presentation content. <br>
Mitigation: Review the generated deck, speaker notes, imported layouts, and theme choices before presenting, exporting, or publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/isatimur/skills/presentation-generator) <br>
- [Presentation-md homepage](https://presentation-md.vercel.app) <br>
- [Presentation-md repository](https://github.com/isatimur/presentation-md) <br>
- [Deck schema](references/deck-schema.md) <br>
- [Theme guide](references/themes.md) <br>
- [Layout recipes](references/layout-recipes.md) <br>
- [Markdown import](references/markdown-import.md) <br>
- [PowerPoint import](references/pptx-import.md) <br>
- [Custom HTML recipes](references/custom-html-recipes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with deck JSON, HTML, PowerPoint, PDF, and shell command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce self-contained HTML decks, editable PowerPoint exports, PDF exports, Markdown conversions, and optional public sharing commands.] <br>

## Skill Version(s): <br>
1.32.2 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
