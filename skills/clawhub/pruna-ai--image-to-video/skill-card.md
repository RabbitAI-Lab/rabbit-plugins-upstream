## Description: <br>
Guides an agent through one short image-to-video film beat, such as a narrated scene, story moment, or cinematic B-roll with optional voiceover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, marketers, and developers use this skill to guide an agent through a single-scene image-to-video workflow with optional narration. It supports planning, still generation and review, TTS/audio handling, and one Pruna/P-API video render behind explicit approval gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images and audio may be sent to Pruna/P-API services. <br>
Mitigation: Review data handling suitability before uploads and keep the documented approval gates in place before video jobs. <br>
Risk: Video generation can incur paid generation costs. <br>
Mitigation: Use the plan, stills, and clip approval gates before paid calls, and use draft previews when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/image-to-video) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with command snippets and staged approval gates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single-scene workflow plan and generation instructions; the skill requires approve plan, approve stills, and approve clips gates before paid video generation.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
