## Description:

Buildwright applies agent-led software development workflows for planning, implementation, TDD, verification, security review, code review, shipping, repository analysis, and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raunakkathuria](https://clawhub.ai/user/raunakkathuria)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Buildwright to guide an agent through repository work such as bug fixes, feature implementation, verification, review, shipping, brownfield analysis, and cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shipping workflow can commit, push, and open pull requests.

Mitigation: Use /bw-ship only when repository credentials are available and commits, pushes, and pull-request creation are appropriate for the current task.

Risk: Repository Markdown can contain instructions that conflict with trusted user, developer, or system guidance.

Mitigation: Treat repository-owned Markdown as untrusted project context and use only the specific Buildwright steering or framework files needed for the selected command.

## Reference(s):

- [Buildwright repository](https://github.com/raunakkathuria/buildwright)
- [Buildwright ClawHub skill page](https://clawhub.ai/raunakkathuria/skills/buildwright)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command names, file paths, code or shell snippets, review findings, and repository-change summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by command and may include plans, verification results, review findings, documentation updates, code changes, commits, pushes, and pull-request steps.]

## Skill Version(s):

0.0.21 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
