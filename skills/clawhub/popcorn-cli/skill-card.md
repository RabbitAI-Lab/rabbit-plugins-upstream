## Description: <br>
Popcorn CLI helps agents use the Popcorn command-line client to list available image and video models, submit asynchronous generation tasks, and check task status and results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeyiy](https://clawhub.ai/user/zeyiy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to automate Popcorn image and video generation workflows from the command line, including model discovery, task submission, and polling for results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Popcorn API key is stored locally in ~/.popcorn-cli/config.json. <br>
Mitigation: Restrict file access, avoid committing or logging the config file, and rotate the key if exposure is suspected. <br>
Risk: Prompts, task parameters, media-generation settings, and session context are sent to the remote Popcorn backend. <br>
Mitigation: Do not include passwords, API keys, private customer data, or confidential business context in prompts or task parameters. <br>
Risk: Task IDs, session IDs, result URLs, and errors may expose business context or generated assets. <br>
Mitigation: Treat command output as sensitive and avoid publishing it in public logs, issues, chat transcripts, or build artifacts. <br>


## Reference(s): <br>
- [Popcorn CLI installation guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Popcorn task IDs, session IDs, result URLs, and status or error details returned by the CLI.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
