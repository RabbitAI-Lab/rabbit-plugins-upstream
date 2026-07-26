## Description: <br>
Authors HyperFrames slideshows, pitch decks, and interactive decks with slides, fragment reveals, branching, hotspot navigation, presenter mode, speaker notes, and page-to-deck conversion guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content authors use this skill to create runnable HyperFrames slideshow decks, convert existing pages into decks, and prepare handoff guidance for presenter-mode use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to silently run an update command that can change installed skills and dependent HyperFrames skills before the user's task. <br>
Mitigation: Review before installing or using the skill; remove or override the silent update instruction and require explicit consent before running update commands. <br>


## Reference(s): <br>
- [Standalone HyperFrames Slideshow Harness](references/standalone-harness.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with HTML, JSON, CSS, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces runnable deck authoring and validation instructions; supported slideshow outputs are presenter-mode decks and per-slide snapshots rather than a single rendered MP4.] <br>

## Skill Version(s): <br>
1.0.7 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
