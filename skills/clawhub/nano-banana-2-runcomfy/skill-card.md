## Description: <br>
Nano Banana 2 on RunComfy helps agents generate text-to-image outputs with Google's flash-tier Gemini image model through the RunComfy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to prepare and run RunComfy CLI image-generation commands for Nano Banana 2 marketing drafts, social thumbnails, batch variants, in-image typography, and selectively web-grounded imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image prompts and generation requests are sent to RunComfy. <br>
Mitigation: Avoid sensitive prompts unless RunComfy is approved for that data, and confirm the provider before running paid or confidential generations. <br>
Risk: The generic "Gemini image" trigger may activate this Nano Banana 2 workflow when another Gemini image provider or model was intended. <br>
Mitigation: Confirm the intended model and provider before invoking the skill, especially for sensitive, high-cost, or production work. <br>
Risk: Web-grounded image generation can add latency, cost, and current-web dependency. <br>
Mitigation: Enable web grounding only when the image prompt needs current events or real-entity context. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/permew/skills/nano-banana-2-runcomfy) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI Documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=nano-banana-2-runcomfy) <br>
- [Nano Banana 2 Model Page](https://www.runcomfy.com/models/google/nano-banana-2?utm_source=clawhub&utm_medium=skill&utm_campaign=nano-banana-2-runcomfy) <br>
- [RunComfy CLI Troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=nano-banana-2-runcomfy) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces image files through the RunComfy CLI output directory; requires runcomfy and either RUNCOMFY_TOKEN or an authenticated RunComfy CLI session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
