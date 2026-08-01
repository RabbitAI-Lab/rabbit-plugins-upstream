## Description: <br>
Generates, inpaints, and outpaints music with ACE Step models on RunComfy through runcomfy CLI guidance for endpoint selection, JSON inputs, and execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and music workflow operators use this skill to generate new tracks, repair time-bounded sections, or extend existing music through RunComfy-hosted ACE Step endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, lyrics, and source audio URLs are sent to RunComfy for generation and editing. <br>
Mitigation: Confirm the operator is comfortable sharing those inputs with RunComfy before execution, and use only user-provided source audio URLs for inpaint and outpaint tasks. <br>
Risk: RUNCOMFY_TOKEN grants access to the operator's RunComfy account. <br>
Mitigation: Protect the token like an API credential; do not echo it into prompts, logs, or committed files. <br>
Risk: Unreviewed shell install scripts can execute code outside the intended RunComfy CLI workflow. <br>
Mitigation: Use the documented npm or npx install path and avoid unreviewed shell install scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/ace-step) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=ace-step) <br>
- [ACE Step text-to-audio on RunComfy](https://www.runcomfy.com/models/acestep-ai/ace-step/text-to-audio?utm_source=clawhub&utm_medium=skill&utm_campaign=ace-step) <br>
- [ACE Step 1.5 text-to-audio on RunComfy](https://www.runcomfy.com/models/acestep-ai/ace-step-1.5/text-to-audio?utm_source=clawhub&utm_medium=skill&utm_campaign=ace-step) <br>
- [ACE Step audio-inpaint on RunComfy](https://www.runcomfy.com/models/acestep-ai/ace-step/audio-inpaint?utm_source=clawhub&utm_medium=skill&utm_campaign=ace-step) <br>
- [ACE Step audio-outpaint on RunComfy](https://www.runcomfy.com/models/acestep-ai/ace-step/audio-outpaint?utm_source=clawhub&utm_medium=skill&utm_campaign=ace-step) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces RunComfy CLI commands and endpoint-specific input guidance; generated audio files are produced by the external RunComfy CLI execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
