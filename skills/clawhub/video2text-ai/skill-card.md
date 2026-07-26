## Description: <br>
Helps agents turn video URLs, local video files, or prior task IDs into transcripts, summaries, rewritten copy, meeting notes, course breakdowns, and other structured video-derived text through an external Guaikei/Qianwen-backed service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[um-why](https://clawhub.ai/user/um-why) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, content teams, and agents use this skill to process online or local videos into cleaned transcripts, summaries, rewrites, interview notes, course outlines, livestream recaps, and other reusable content assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads user videos to an external service while making retention and privacy claims that local code does not enforce. <br>
Mitigation: Use only videos that are acceptable to send to the provider, and verify the provider's retention, deletion, and training policy outside the skill text before sensitive use. <br>
Risk: Broad file, URL, and prior task ID handling can trigger unintended paid processing. <br>
Mitigation: Require explicit user confirmation before processing local paths, remote URLs, previous task IDs, or any action that may incur charges. <br>
Risk: The skill requires a provider API token to operate. <br>
Mitigation: Keep GUAIKEI_API_TOKEN in the environment or a managed secret store and avoid placing it in prompts, command history, logs, or shared files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/um-why/skills/video2text-ai) <br>
- [Guaikei website](https://www.guaikei.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [CLI stdout containing generated video text, with shell command invocations for file, URL, task ID, and prompt-based workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and GUAIKEI_API_TOKEN; processing can use --file, --id, and --prompt inputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata, package.json, constants.js) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
