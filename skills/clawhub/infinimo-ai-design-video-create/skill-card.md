## Description: <br>
Generate AI video via Infinimo AI Design using prompt-only, first/last frame, or uploaded asset workflows with model discovery, credit estimates, uploads, job submission, and result polling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to submit Infinimo text-to-video, image-to-video, and frame-to-frame generation jobs, estimate credits, upload selected media assets, and retrieve generated video URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected media files are sent to the Infinimo/clawec.com API using the user's API token. <br>
Mitigation: Avoid uploading sensitive or private media unless the provider's retention and privacy terms are acceptable. <br>
Risk: The documented delete endpoint can remove remote generation history or results. <br>
Mitigation: Treat deletion as a manual destructive action and confirm the target record before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/infinimo-ai-design-video-create) <br>
- [Infinimo AI Design](https://design.infinimo.ai/?source=q-i-d-clawhub) <br>
- [Response schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns generated video URLs and request summaries after polling the provider API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
