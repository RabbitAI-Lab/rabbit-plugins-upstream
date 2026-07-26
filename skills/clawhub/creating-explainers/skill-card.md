## Description: <br>
Creates single-file interactive HTML explainers with hand-built Canvas figures from supplied documents, researched topics, or mixed source material. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[analyticalmonk](https://clawhub.ai/user/analyticalmonk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, educators, and agents use this skill to turn papers, reports, transcripts, or researched topics into browser-ready interactive explainers with source-grounded prose and Canvas figures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad visual-explanation requests when the user wanted a simpler response. <br>
Mitigation: Confirm the user wants an interactive explainer and use the required outline approval step before drafting. <br>
Risk: Topic-driven explainers can contain unsupported factual claims if sources are unavailable or unchecked. <br>
Mitigation: Use provided files or researched sources as the source of truth and complete the required research-time and post-draft fact-check gates. <br>
Risk: Generated single-file HTML with hand-written Canvas interactions can fail to render or respond correctly. <br>
Mitigation: Run the artifact's local browser checks when possible, or at minimum check matching element IDs, Canvas initialization, controls, and responsive behavior before delivery. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/analyticalmonk/skills/creating-explainers) <br>
- [Article Template](assets/article-template.html) <br>
- [Template Walkthrough](references/template-walkthrough.md) <br>
- [Figure Archetypes](references/figure-archetypes.md) <br>
- [Voice and Style](references/voice-and-style.md) <br>
- [Intake From Files](references/intake-from-files.md) <br>
- [Intake From Research](references/intake-from-research.md) <br>
- [Color Palettes](references/color-palettes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus a self-contained HTML/CSS/JavaScript file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one browser-openable index.html with inline CSS, inline JavaScript, Canvas figures, and no build step.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
