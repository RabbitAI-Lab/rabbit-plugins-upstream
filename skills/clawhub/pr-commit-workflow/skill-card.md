## Description: <br>
This skill should be used when creating commits or pull requests, enforcing a human-written PR structure, intent capture, and evidence in agentic workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joshp123](https://clawhub.ai/user/joshp123) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
Developers and coding agents use this skill when preparing commits and pull requests to capture human intent, test evidence, prompt history, and review-ready change summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt history and local environment details in PR bodies can expose sensitive information. <br>
Mitigation: Manually review and redact prompt history, terminal details, system information, internal paths, tokens, secrets, and private business context before publishing a PR. <br>
Risk: The workflow can publish user and agent conversation history to public or sensitive repositories. <br>
Mitigation: Require explicit approval before adding transcript or environment details to a PR, and avoid using the workflow unchanged on public or sensitive repositories. <br>


## Reference(s): <br>
- [Commit Workflow](references/workflow-commit.md) <br>
- [PR Workflow](references/workflow-pr.md) <br>
- [Human PR Template](references/pr-human-template.md) <br>
- [Commit Message Format](references/commit-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with commit message templates, PR body sections, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-written PR intent and may include environment metadata and prompt history.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
