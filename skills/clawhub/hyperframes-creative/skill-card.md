## Description: <br>
Provides non-animation creative direction for HyperFrames videos, covering design specs, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand or style decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative teams use this skill to plan the brand, pacing, style, narration, and frame composition of HyperFrames videos after the technical contract is in place. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run local scripts and process audio or video through ffmpeg. <br>
Mitigation: Review commands before execution and run them only on trusted media in a controlled project workspace. <br>
Risk: Preview or showcase HTML may start a localhost server and load Google Fonts or jsdelivr assets. <br>
Mitigation: Use network controls in stricter environments and avoid opening preview HTML unless external asset access is acceptable. <br>
Risk: Creative tooling may write design files, generated reports, or other project artifacts. <br>
Mitigation: Review changed files before committing and pin HYPERFRAMES_SKILL_PKG_VERSION when bootstrapping dependencies outside the bundled CLI. <br>


## Reference(s): <br>
- [House Style](artifact/references/house-style.md) <br>
- [Video Composition](artifact/references/video-composition.md) <br>
- [Design Spec](artifact/references/design-spec.md) <br>
- [Visual Style Library](artifact/references/visual-styles.md) <br>
- [Beat Direction](artifact/references/beat-direction.md) <br>
- [Audio-Reactive Animation](artifact/references/audio-reactive.md) <br>
- [Typography](artifact/references/typography.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-creative) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write design spec files, generate HTML/CSS direction, and provide local script commands for HyperFrames workflows.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
