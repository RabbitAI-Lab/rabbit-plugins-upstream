## Description: <br>
Generate videos with Google Veo models through the inference.sh CLI, including Veo 3.1, Veo 3.1 Fast, Veo 3, Veo 3 Fast, and Veo 2. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to generate video clips from text prompts with Google Veo models via the inference.sh CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing and logging into the inference.sh CLI carries normal third-party CLI distribution and account-login risks. <br>
Mitigation: Install only if inference.sh is trusted, use the intended account for infsh login, and verify CLI checksums manually when practical. <br>
Risk: Prompts and input files used for video generation may be sent to an external video-generation service. <br>
Mitigation: Avoid including confidential material in prompts or input files submitted for generation. <br>


## Reference(s): <br>
- [Google Veo ClawHub Skill](https://clawhub.ai/okaris/skills/google-veo) <br>
- [inference.sh](https://inference.sh) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Streaming Results](https://inference.sh/docs/api/sdk/streaming) <br>
- [Content Pipeline Example](https://inference.sh/docs/examples/content-pipeline) <br>
- [inference.sh CLI Checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the inference.sh CLI and may reference prompt JSON input files.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
