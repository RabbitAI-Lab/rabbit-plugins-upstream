## Description: <br>
Generate a two-speaker conversation as a single audio file with natural turn-taking using inline speaker tags mapped to two voice model IDs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to guide an agent in preparing and submitting a two-speaker dialogue audio generation request, such as a podcast snippet, interview, explainer, or character exchange. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, scripts, and selected voice model IDs may be sent to an external audio generation provider. <br>
Mitigation: Avoid sensitive content in prompts or scripts unless the provider is approved for that data. <br>
Risk: Generated dialogue can use recognizable or cloned voices without appropriate permission. <br>
Mitigation: Use only voice models that the user has rights or consent to use, especially for recognizable voices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/dialogue-audio) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/runware) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API Calls, configuration] <br>
**Output Format:** [Markdown guidance with model parameters and request workflow details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent guidance for text-to-audio dialogue requests; the downstream audio generation provider returns the final audio URL.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
