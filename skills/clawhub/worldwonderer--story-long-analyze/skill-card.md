## Description: <br>
Analyzes long-form web novels through a staged pipeline covering opening chapters, character structure, reader-payoff design, pacing, chapter summaries, setting and relationship extraction, summary reports, and style profiling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and creative-development agents use this skill to break down legally available long-form fiction into structured analysis files for plot, pacing, character, setting, emotional hooks, reusable writing patterns, and prose style. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill copies full novel text into the workspace and stores sizeable source excerpts. <br>
Mitigation: Use it only with text you own or are authorized to process, and delete retained `原文/`, `文风.md` excerpts, and `/tmp/style-sample.txt` when source text should not remain on disk. <br>
Risk: The skill can update related project files outside the main analysis folder without a strong confirmation step. <br>
Mitigation: Run it in a controlled workspace and review diffs after each run before accepting or publishing changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-analyze) <br>
- [Publisher profile](https://clawhub.ai/user/worldwonderer) <br>
- [OpenClaw source metadata link](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Material decomposition reference](references/material-decomposition.md) <br>
- [Output templates reference](references/output-templates.md) <br>
- [Style profile protocol reference](references/style-profile-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Analysis, Guidance] <br>
**Output Format:** [Markdown files organized under a book-specific analysis directory] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates staged analysis artifacts such as summaries, character files, plot and pacing indexes, setting notes, reports, progress state, and style profiles.] <br>

## Skill Version(s): <br>
1.1.12 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
