## Description: <br>
Generate and remix images with Flux 2 through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate or remix Flux 2 images through RunAPI, choosing CLI commands for one-off work and SDK integration guidance for application or backend use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, source images, and API credentials are sent to or used with RunAPI services. <br>
Mitigation: Use the skill only when RunAPI is trusted for the submitted content, and prefer the RUNAPI_API_KEY environment variable for headless or agent use. <br>
Risk: Using the CLI as a production integration layer can create fragile service behavior. <br>
Mitigation: Use RunAPI SDK packages for application, backend, worker, or production integrations. <br>
Risk: Generated file URLs are temporary and may expire. <br>
Mitigation: Download generated images and store them in durable storage within 7 days. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-flux-2) <br>
- [RunAPI Flux 2 homepage](https://runapi.ai/models/flux-2) <br>
- [RunAPI Flux 2 model documentation](https://runapi.ai/models/flux-2.md) <br>
- [Black Forest Labs provider page](https://runapi.ai/providers/black-forest-labs.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK package names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference temporary generated-file URLs that should be downloaded to durable storage within 7 days.] <br>

## Skill Version(s): <br>
0.3.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
