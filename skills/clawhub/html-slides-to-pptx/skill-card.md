## Description: <br>
Creates validated HTML slide decks from a guided brief and converts them into PowerPoint presentations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqcmj74](https://clawhub.ai/user/cqcmj74) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to gather presentation requirements, create an HTML slide project, validate slide structure and visual quality, and convert the result to PPTX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses Node, npm, Playwright, and a browser-based conversion pipeline. <br>
Mitigation: Install and run it only in environments where those local tools and dependency downloads are acceptable. <br>
Risk: Slide conversion may load remote image or font URLs and local media paths referenced by a deck. <br>
Mitigation: Use trusted slide projects and review remote URLs and local media paths before previewing or converting. <br>
Risk: Generated deck files, previews, caches, and PPTX outputs are written under the deck directory. <br>
Mitigation: Run the skill in an intended working directory and review generated files before sharing them. <br>
Risk: Only the documented HTML and CSS subset is intended to convert cleanly to PPTX. <br>
Mitigation: Run the bundled validator and preview workflow, fix all errors, and review acceptable warnings before conversion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cqcmj74/skills/html-slides-to-pptx) <br>
- [HTML slide specification](reference/html-spec.md) <br>
- [Design principles](reference/design-principles.md) <br>
- [Interview guide](reference/interview-guide.md) <br>
- [Page archetypes](reference/page-archetypes.md) <br>
- [Behavior baseline](reference/behavior-baseline.md) <br>
- [Theme presets](reference/theme-presets.md) <br>
- [VoltAgent awesome-design-md](https://github.com/VoltAgent/awesome-design-md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands plus generated HTML, CSS, JSON, PNG preview, and PPTX files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm; first use may install Node dependencies and Playwright Chromium.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
