## Description: <br>
Turns briefs, links, or research topics into controlled, source-grounded video prompts for HiAPI Seedance 2.0 or HappyHorse 1.0. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hiapiai](https://clawhub.ai/user/hiapiai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and AI-agent users use this skill to turn short video briefs, URLs, GitHub repositories, documents, or research topics into structured, scene-by-scene prompts and handoff commands for HiAPI video-generation skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer and update flow can modify local agent skill directories. <br>
Mitigation: Review the skill files before installation and prefer a scoped or manual install target when directory changes need tighter control. <br>
Risk: The update check can present remotely supplied update commands. <br>
Mitigation: Inspect update commands before running them, and disable the update check with HIAPI_SKIP_UPDATE_CHECK=1 where automatic checks are not appropriate. <br>
Risk: Prompts and handoff commands may carry sensitive user material to downstream HiAPI render skills. <br>
Mitigation: Do not include secrets, private URLs, unreleased business plans, confidential media references, or credentials in generated prompts or commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hiapiai/hiapi-video-prompt-generator) <br>
- [HiAPI Documentation](https://docs.hiapi.ai) <br>
- [HiAPI Seedance 2.0 Video Skill](https://github.com/HiAPIAI/hiapi-seedance-2-0-video-skill) <br>
- [HiAPI HappyHorse 1.0 Video Skill](https://github.com/HiAPIAI/hiapi-happyhorse-1-0-video-skill) <br>
- [HiAPI Skills](https://github.com/HiAPIAI/hiapi-skills) <br>
- [Prompt Patterns](references/prompt-patterns.md) <br>
- [Source Extraction](references/source-extraction.md) <br>
- [HiAPI Handoff](references/hiapi-handoff.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with structured sections and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes model-specific HiAPI duration, resolution, aspect, media-mode, negative-constraint, and handoff-command details.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; package.json reports 0.1.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
