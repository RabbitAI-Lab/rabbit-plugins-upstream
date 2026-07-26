## Description: <br>
Generates deep technical CookBooks, Handbooks, and Surveys from user materials such as websites, PDFs, EPUBs, GitHub repositories, arxiv papers, and documentation, then produces MDX chapters first with optional ElegantBook LaTeX/PDF, Nextra website, and optimized EPUB outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and documentation teams use this skill to turn multi-source technical material into structured long-form books, handbooks, surveys, and multi-format documentation packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram rendering helpers can send diagram content to kroki.io. <br>
Mitigation: Confirm diagrams are safe to share externally before remote rendering, or use a local renderer such as Docker-based PlantUML for private material. <br>
Risk: A generated PlantUML rendering command is unsafe with untrusted filenames. <br>
Mitigation: Use trusted or sanitized filenames and review generated commands before executing diagram rendering. <br>
Risk: Generated Nextra site dependencies may age or contain deploy-time vulnerabilities. <br>
Mitigation: Audit, pin, and update the generated site dependencies before publishing or deploying the Nextra output. <br>
Risk: Generated prompt and conversion files may copy source content into derivative outputs. <br>
Mitigation: Review generated files for confidential, licensed, or source-sensitive material before distribution. <br>


## Reference(s): <br>
- [O'Reilly CookBook Style Guide](references/style-guide-oreilly.md) <br>
- [Springer Handbook Style Guide](references/style-guide-springer.md) <br>
- [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook) <br>
- [Kroki PlantUML Rendering Endpoint](https://kroki.io/plantuml/svg/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [MDX and Markdown source files, LaTeX/PDF project files, Nextra site files, EPUB assets, and command-oriented guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is MDX; PDF, Nextra site, and EPUB outputs are generated when requested.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
