## Description: <br>
Delegates tasks to Gemini CLI implementing delegation-core for Google's models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to delegate batch processing, summarization, pattern extraction, and large-context file analysis tasks to the Gemini CLI after delegation-core selects Gemini as suitable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gemini CLI examples can send local file contents to Google Gemini, including files matched by @path or recursive glob patterns. <br>
Mitigation: Review included paths before execution and avoid sending secrets, credentials, private customer data, or proprietary code unless policy allows it. <br>
Risk: Large recursive file inclusions can unintentionally include more data than needed for the delegation task. <br>
Mitigation: Use selective file paths or narrow glob patterns and inspect the target file set before running the Gemini CLI command. <br>


## Reference(s): <br>
- [Gemini-Specific Configuration](modules/gemini-specifics.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-conjure-gemini-delegation) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Gemini CLI commands, model-selection guidance, authentication steps, and file inclusion patterns.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
