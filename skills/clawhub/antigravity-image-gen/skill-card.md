## Description: <br>
Generates images through the Google Antigravity API using Gemini 3 Pro Image and local OAuth credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ipedrax](https://clawhub.ai/user/ipedrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to generate image files from natural-language prompts in workflows that have an authorized Google Antigravity OAuth profile available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a local Google Antigravity OAuth profile to authenticate requests. <br>
Mitigation: Install it only when you intend image-generation prompts to use that local profile, and review the selected auth profile before running it. <br>
Risk: Prompts are sent to a Google sandbox endpoint under the configured account. <br>
Mitigation: Do not send sensitive prompts unless that endpoint and account usage are approved for the environment. <br>
Risk: The request uses bypass-oriented headers that may not be acceptable in all environments. <br>
Mitigation: Review the request behavior and headers against local policy before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ipedrax/skills/antigravity-image-gen) <br>
- [Google Cloud Code sandbox generation endpoint](https://daily-cloudcode-pa.sandbox.googleapis.com/v1internal:streamGenerateContent?alt=sse) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text] <br>
**Output Format:** [PNG image file with stdout status messages and a MEDIA path marker] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports prompt, output path, and aspect ratio options.] <br>

## Skill Version(s): <br>
2.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
