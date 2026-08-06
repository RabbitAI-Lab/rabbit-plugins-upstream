## Description: <br>
Generate polished slide decks as self-contained HTML and editable PowerPoint from notes, using structured deck JSON, curated themes, layout recipes, and export tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[isatimur](https://clawhub.ai/user/isatimur) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and presentation authors use this skill to turn notes or briefs into polished slide decks for pitches, investor updates, keynotes, product launches, sales demos, and related presentation workflows. It can guide agents to create deck JSON, render HTML, export editable PowerPoint, import Markdown or PowerPoint, and optionally export PDF or deploy a deck. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install Node-based rendering dependencies and use browser automation for PDF export. <br>
Mitigation: Run export workflows in a trusted environment and review generated files and commands before execution. <br>
Risk: The deployment workflow can publish decks to externally visible Vercel URLs. <br>
Mitigation: Confirm the deck contains no confidential material and get explicit approval before deployment, especially for production publication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/isatimur/skills/presentation-md) <br>
- [Server-Resolved Source Provenance](https://github.com/isatimur/presentation-md/tree/main/skills/presentation-generator) <br>
- [Project Homepage](https://presentation-md.vercel.app) <br>
- [Presentation MD Studio](https://presentation-md.vercel.app/studio) <br>
- [Repository](https://github.com/isatimur/presentation-md) <br>
- [Deck Schema](references/deck-schema.md) <br>
- [Theme Reference](references/themes.md) <br>
- [Layout Recipes](references/layout-recipes.md) <br>
- [Markdown Import](references/markdown-import.md) <br>
- [PowerPoint Import](references/pptx-import.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with deck JSON, HTML, PowerPoint export instructions, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce self-contained HTML decks, editable PPTX exports, PDF exports, imported deck JSON, and deployment commands depending on the workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata); artifact metadata reports 1.32.2 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
