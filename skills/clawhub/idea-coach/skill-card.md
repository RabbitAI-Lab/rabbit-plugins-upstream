## Description: <br>
AI-powered idea/problem/challenge manager with GitHub integration. Captures, categorizes, reviews, and helps ship ideas to repos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Idea Coach to capture ideas, problems, and challenges, review them on a schedule, and optionally connect them to GitHub repositories or issues when ready to ship. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Idea notes may contain sensitive plans or personal context because the skill stores entries locally and can sync selected ideas to GitHub issues. <br>
Mitigation: Avoid storing secrets or highly confidential plans, and review issue content before syncing it to GitHub. <br>
Risk: GitHub operations use the currently authenticated gh CLI identity and can create public repositories when requested. <br>
Mitigation: Check the active GitHub account and repository visibility before linking, creating, or syncing repositories. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/udiedrichsen/skills/idea-coach) <br>
- [README](artifact/README.md) <br>
- [Concept](artifact/CONCEPT.md) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-like command output with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores idea records locally and can invoke GitHub CLI commands when users request repository or issue operations.] <br>

## Skill Version(s): <br>
0.2.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
