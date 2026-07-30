## Description: <br>
RunComfy CLI on RunComfy teaches agents how to install and authenticate the runcomfy CLI, discover model schemas, invoke RunComfy image, video, edit, and training endpoints, poll or submit jobs, handle JSON output, and manage CLI errors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to install, authenticate, and script the RunComfy CLI for model invocation, status polling, JSON output, and generated media downloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunComfy tokens can be exposed if logged, echoed into prompts, or committed to a repository. <br>
Mitigation: Treat RUNCOMFY_TOKEN and the local RunComfy token file like API keys; avoid logging tokens and rotate credentials if exposure is suspected. <br>
Risk: A non-npm installer path may execute remote installation code. <br>
Mitigation: Use the documented npm or npx installation paths when possible, and review any standalone installer before running it. <br>
Risk: Model results download to disk by default and may be written to an unintended location. <br>
Mitigation: Choose output directories deliberately, use no-download behavior when only result JSON is needed, and account for generated file size. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/runcomfy-cli) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>
- [RunComfy CLI install guide](https://docs.runcomfy.com/cli/install?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>
- [RunComfy CLI authentication](https://docs.runcomfy.com/cli/auth?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>
- [RunComfy CLI quickstart](https://docs.runcomfy.com/cli/quickstart?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>
- [RunComfy command reference](https://docs.runcomfy.com/cli/commands?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>
- [RunComfy troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>
- [RunComfy model catalog](https://www.runcomfy.com/models?utm_source=clawhub&utm_medium=skill&utm_campaign=runcomfy-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command flags, JSON request examples, output directory guidance, authentication notes, and troubleshooting patterns.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
