## Description: <br>
Analyzes ZenTao bug reports by extracting Bug links from Feishu messages, collecting issue details and attachments, locating relevant code versions, and producing root-cause reports with optional ZenTao comments and Feishu summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yeah526](https://clawhub.ai/user/yeah526) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to triage ZenTao defects, gather logs and attachments, map bugs to configured local code modules, and prepare Markdown root-cause analysis reports for review or posting back to ZenTao. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an authenticated ZenTao session and stores a ZenTao password in local configuration. <br>
Mitigation: Keep bug-analyzer-config.json out of source control, restrict file permissions, use appropriate account access, and clean up the browser session after each run. <br>
Risk: The skill can automatically post analysis results to ZenTao when auto_comment is enabled. <br>
Mitigation: Set auto_comment to false until reports have been reviewed, then enable posting only for trusted workflows. <br>
Risk: The workflow checks out commits and may create local worktrees while analyzing code. <br>
Mitigation: Run analysis in an isolated working tree or disposable checkout and confirm the target repository state before reusing it. <br>


## Reference(s): <br>
- [ZenTao API Reference](references/zentao-api-reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/yeah526/skills/zentao-bug-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with supporting shell commands, JSON script output, and generated HTML comments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write per-bug report and comment files under bugs/<bug_id>/ and may post comments when auto_comment is enabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
