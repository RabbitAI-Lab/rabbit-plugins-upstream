## Description: <br>
HappyHorse 1.0 is a text-to-video generation skill that guides an agent to call the RunComfy CLI endpoint for native 1080p video with in-pass synchronized audio and multi-shot character consistency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to generate short text-to-video clips through RunComfy with prompts, aspect ratio, duration, resolution, seed, and watermark controls. It is best suited for multi-shot stories, synchronized audio/video clips, multilingual short-form content, and iterative video prompt design. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts are sent to RunComfy's hosted model service. <br>
Mitigation: Confirm the user trusts RunComfy and is comfortable sending the prompt content to that service before running the CLI. <br>
Risk: The skill depends on a RunComfy CLI installation and an API token. <br>
Mitigation: Install the CLI from the documented source and use the documented login flow or RUNCOMFY_TOKEN handling appropriate for the environment. <br>
Risk: Generated videos can be large and may consume local disk space. <br>
Mitigation: Choose output directories deliberately and monitor available disk space for longer or higher-resolution generations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/permew/skills/happyhorse-1-0) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI Introduction](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=happyhorse-1-0) <br>
- [HappyHorse 1.0 Text-to-Video on RunComfy](https://www.runcomfy.com/models/happyhorse/happyhorse-1-0/text-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=happyhorse-1-0) <br>
- [RunComfy CLI Troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=happyhorse-1-0) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash command examples and JSON input snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides RunComfy CLI invocations that submit video requests and download generated output files to a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
