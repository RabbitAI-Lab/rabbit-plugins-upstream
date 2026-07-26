## Description: <br>
Nano Triple helps an agent generate three parallel image options from the same prompt so the user can compare, pick, or refine the result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to create three distinct image candidates from one image prompt, then select a preferred option or request another three-option refinement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt text may be passed into shell command examples when generating images. <br>
Mitigation: Invoke the skill intentionally, avoid untrusted prompt text in shell commands, and ensure prompt values are passed as safely quoted arguments. <br>


## Reference(s): <br>
- [Google AI Studio](https://aistudio.google.com) <br>
- [ClawHub skill page](https://clawhub.ai/mvanhorn/skills/nano-triple) <br>


## Skill Output: <br>
**Output Type(s):** [Images, Shell commands, Guidance] <br>
**Output Format:** [Three labeled generated images with concise text and markdown bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the same user prompt for three parallel image generations; uses GEMINI_API_KEY from the environment or OpenClaw config.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; SKILL.md frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
