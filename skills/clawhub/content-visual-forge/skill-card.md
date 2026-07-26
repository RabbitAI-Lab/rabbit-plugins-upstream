## Description: <br>
Content Visual Forge helps agents turn PDFs, web pages, articles, screenshots, transcripts, images, characters, and vocabulary lists into structured visual-content plans such as WeChat covers, knowledge cards, character cards, vocabulary cards, social cards, and render packages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fxbin](https://clawhub.ai/user/fxbin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-producing agents use this skill to analyze source material, lock the current source, choose an output mode, and prepare visual asset prompts or engineering render packages for publication workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad visual-content activation may produce poor results if source material, platform, language, size, or rendering path is ambiguous. <br>
Mitigation: Specify the source material, target platform, language, output size, and whether image generation or engineering rendering should be used before execution. <br>
Risk: Generated visual assets can misrepresent source content or make text unreadable when fidelity requirements are high. <br>
Mitigation: Use the skill's source-lock, content-fidelity, engineering-rendering, and quality-gate steps before publishing or batch production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fxbin/skills/content-visual-forge) <br>
- [Server-resolved GitHub source](https://github.com/fxbin/skills/tree/main/content-visual-forge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured visual briefs, prompt packages, render specifications, and optional code or shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires source lock, declared output mode, declared execution mode, and quality review before final asset generation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
