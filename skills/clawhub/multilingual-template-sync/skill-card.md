## Description: <br>
Helps agents update multilingual customer service response templates, publish them to Feishu Wiki, and create GitHub issues to track documentation and internationalization changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer support, documentation, and localization teams use this skill to add or scaffold new language sections in markdown response templates, publish updated content to Feishu Wiki, and open GitHub issues for tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A selected local file could contain secrets or private customer data and be uploaded to Feishu Wiki. <br>
Mitigation: Inspect the file before syncing, restrict the script to approved template paths, and use a least-privilege Feishu app limited to the intended wiki space. <br>
Risk: A write-capable GitHub token could create issues in the wrong repository or with unintended content. <br>
Mitigation: Use a least-privilege token, confirm the repository, title, and issue body before execution, and review the resulting issue URL. <br>
Risk: Credential environment variables are required for Feishu and GitHub operations. <br>
Mitigation: Provide credentials only at runtime, avoid committing or echoing them, and rotate them if they may have been exposed. <br>


## Reference(s): <br>
- [Workflow Reference](references/workflow.md) <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/multilingual-template-sync) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown edits with shell command and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May also create external Feishu Wiki content and GitHub issues when the user runs the provided scripts with credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
