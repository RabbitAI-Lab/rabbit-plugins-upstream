## Description: <br>
Analyzes code changes and drafts Conventional Commits messages and pull request descriptions in Chinese or English. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yang1002378395-cmyk](https://clawhub.ai/user/yang1002378395-cmyk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to turn selected diffs, changed files, branch context, or issue references into readable commit messages and pull request descriptions that follow Conventional Commits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private repository context can be exposed if the user provides unrelated diffs, files, branches, or issue references. <br>
Mitigation: Invoke the skill deliberately and provide only the repository context that should be considered for the commit message or pull request description. <br>
Risk: Generated commit messages or pull request descriptions can misstate the intent, testing status, breaking-change impact, or issue closure behavior of a change. <br>
Mitigation: Review and edit the generated text before committing or opening a pull request. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/yang1002378395-cmyk/git-commit-helper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text containing Conventional Commits messages, optional commit bodies and footers, and pull request descriptions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Chinese or English text, issue references, breaking-change notes, and review checklists when supplied by the user.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
