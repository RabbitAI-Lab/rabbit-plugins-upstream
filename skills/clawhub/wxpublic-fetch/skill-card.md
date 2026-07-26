## Description: <br>
Fetches WeChat public account articles for a requested account and date range, then saves the results as local Markdown files for later reading, summarization, or question answering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiongweixp](https://clawhub.ai/user/xiongweixp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content analysts use this skill to collect WeChat public account articles into local Markdown files and retain the saved paths for follow-up summarization or Q&A. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credentials, queried account names, date ranges, and article URLs are sent to third-party services. <br>
Mitigation: Use environment variables for credentials where possible, avoid command-line secrets, and run the skill only when sharing that request data with the referenced services is acceptable. <br>
Risk: The skill downloads remote-selected images and writes article files into a local output directory. <br>
Mitigation: Use a dedicated output directory, review generated files before reuse, and run the skill only in environments where remote downloads and local file writes are allowed. <br>
Risk: The server security verdict is suspicious. <br>
Mitigation: Review the skill before installing or running it, and apply the server security guidance during deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiongweixp/skills/wxpublic-fetch) <br>
- [Publisher profile](https://clawhub.ai/user/xiongweixp) <br>
- [WeChat public account service](https://wxpub.aibana.art/) <br>
- [Markdown conversion service](https://anything-md.doocs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files with downloaded images plus a text summary of saved and failed article paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes article files and images to the configured local output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
