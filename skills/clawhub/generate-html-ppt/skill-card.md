## Description:

Generate HTML PPT helps agents create or convert PowerPoint decks into responsive, design-system-driven HTML presentations for English and Chinese presentation requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agent users use this skill to build new HTML slide decks, convert PPTX files, or derive social media covers from presentation content while following a staged outline, style preview, wireframe, and verification workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates local HTML and asset files and may overwrite existing work if paths are reused.

Mitigation: Use a dedicated project folder and confirm output filenames before allowing file creation or replacement.

Risk: PPTX conversion parses provided slide content, including speaker notes and embedded images.

Mitigation: Review source decks for confidential or sensitive material before processing them with the skill.

Risk: Generated decks may load fonts or JavaScript libraries from public CDNs.

Mitigation: For restricted or offline environments, make fonts and JavaScript dependencies local before sharing or presenting the deck.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/helloyxs/generate-html-ppt)
- [ClawHub skill page](https://clawhub.ai/helloyxs/skills/generate-html-ppt)
- [README_en.md](README_en.md)
- [SKILL.md](SKILL.md)
- [Bold template selection index](designs/bold-template-pack/selection-index.json)
- [Presentation quality checklist](references/checklist.md)
- [Screenshot framing guide](references/screenshot-framing.md)
- [PowerPoint extraction script](scripts/extract-pptx.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated HTML, CSS, JavaScript, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local presentation files and assets; PPTX conversion may parse slide text, images, and speaker notes.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
