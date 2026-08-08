## Description: <br>
Generate HTML visualization reports. Simple mode: single-page responsive (Tailwind+Mermaid). Complex mode: multi-page fixed 1017x720px with 13+ SVG charts and Chrome screenshot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and report authors use this skill to turn analysis, review findings, project health information, or presentation material into HTML visualization reports. It supports quick single-page reports and formal multi-page fixed-size report decks with charts and screenshot validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML may load external CDNs or fonts. <br>
Mitigation: Review external dependencies before use, and replace or inline assets when reports must be private, offline, or tightly controlled. <br>
Risk: Generated report files and screenshots may contain private or sensitive information. <br>
Mitigation: Review generated HTML and screenshots before sharing, and store outputs only in approved locations. <br>
Risk: Complex-mode screenshot workflows may use a headless browser. <br>
Mitigation: Run screenshot validation in a controlled workspace and inspect generated outputs before distribution. <br>
Risk: The skill may search the web for unfamiliar diagram structures. <br>
Mitigation: Avoid sending sensitive report content in search queries and verify any externally sourced diagram structure before using it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/html-report) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Canvas and structure rules](artifact/templates/complex/01-canvas.md) <br>
- [Design system and visual templates](artifact/templates/complex/02-design-system.md) <br>
- [Layout system](artifact/templates/complex/03-layout.md) <br>
- [Color and font system](artifact/templates/complex/04-color-font.md) <br>
- [Content rules and chart library](artifact/templates/complex/05-content.md) <br>
- [Workflow and quality checks](artifact/templates/complex/06-workflow.md) <br>
- [Special page specifications](artifact/templates/complex/07-special-pages.md) <br>
- [Extended SVG chart library](artifact/templates/complex/08-svg-extended.md) <br>
- [Component library](artifact/templates/complex/09-components.md) <br>
- [Business diagram library](artifact/templates/complex/10-diagram-types.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [HTML report files with Markdown guidance and shell commands for screenshot validation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Simple mode produces a single responsive HTML file; complex mode produces fixed 1017x720px multi-page HTML reports and may produce screenshots.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
