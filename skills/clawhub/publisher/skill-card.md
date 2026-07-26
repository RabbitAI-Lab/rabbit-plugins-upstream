## Description: <br>
Make your skills easy to understand and impossible to ignore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tunaissacoding](https://clawhub.ai/user/tunaissacoding) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and skill publishers use Publisher to generate clearer README copy and one-line descriptions, then publish skill directories to GitHub and ClawHub from a shell workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit local skill files and publish the directory to public services. <br>
Mitigation: Inspect the skill directory before approving publication, remove secrets or private files, and confirm .gitignore excludes anything that should not be published. <br>
Risk: Publishing depends on authenticated GitHub and ClawHub command-line tools. <br>
Mitigation: Run it only in the intended skill directory and verify the repository target before accepting the publish prompt. <br>


## Reference(s): <br>
- [GitHub documentation best practices](https://docs.github.com/en/contributing/writing-for-github-docs/best-practices-for-github-docs) <br>
- [Publisher on ClawHub](https://clawhub.ai/tunaissacoding/skills/publisher) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and command-line prompts with generated file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May edit SKILL.md, generate README.md, initialize git, push code, and publish to ClawHub after user approval.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
