## Description: <br>
Publication-grade Chinese long-form novel creation skill covering story setup, worldbuilding, character design, outlining, chapter drafting, foreshadowing management, and quality control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbroot](https://clawhub.ai/user/bbroot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External authors and writing-focused agents use this skill to plan, draft, and revise Chinese fiction, especially long-form novels that need structured outlines, character continuity, foreshadowing tracking, and chapter quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project or character names containing slashes, absolute paths, or ../ can cause state-management scripts to write outside the intended novel workspace. <br>
Mitigation: Use simple book and character names without path separators, review generated paths before running helper scripts, and run the skill only where persistent novel project files are expected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bbroot/skills/novel-master-v2) <br>
- [README](README.md) <br>
- [English README](README_EN.md) <br>
- [Plot structure](references/plot-structure.md) <br>
- [Character design](references/character-design.md) <br>
- [Style guide](references/style-guide.md) <br>
- [Scene writing](references/scene-writing.md) <br>
- [Foreshadowing](references/foreshadowing.md) <br>
- [Genres](references/genres.md) <br>
- [Banned words](references/banned-words.md) <br>
- [Dramaturgy](references/dramaturgy.md) <br>
- [Classic writing books](references/classic-writing-books.md) <br>
- [Process per character](references/process-per-character.md) <br>
- [Node compressed graph](references/node-compressed-graph.md) <br>
- [Quantum auditor](references/quantum-auditor.md) <br>
- [Cognitive bias](references/cognitive-bias.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create and update state files under ~/.qclaw/workspace/novels when helper scripts are used.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
