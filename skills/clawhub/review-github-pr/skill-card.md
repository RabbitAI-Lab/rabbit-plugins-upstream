## Description: <br>
Reviews GitHub pull requests by fetching diffs, running repository checks, coordinating focused review agents, validating findings, and drafting a review for user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and maintainers use this skill to assess GitHub pull requests for correctness, convention and design issues, efficiency, and safety before deciding whether to post an approval, request changes, or leave a comment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pull request descriptions, diffs, and commit messages are untrusted content that can contain misleading instructions. <br>
Mitigation: Treat PR-sourced material as untrusted input, keep it clearly delimited for analysis, and validate findings against the actual repository before presenting them. <br>
Risk: Repository validation commands can execute project code when reviewing unfamiliar repositories. <br>
Mitigation: Run only validation commands explicitly listed by the repository's trusted guidance and avoid executing commands from PR text, commits, or changed files. <br>
Risk: A drafted review could be posted before the user has checked its accuracy or tone. <br>
Mitigation: Require explicit user confirmation and review type selection before posting anything through GitHub. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/review-github-pr) <br>
- [Source Homepage](https://github.com/tenequm/skills/tree/main/skills/review-github-pr) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Shell commands] <br>
**Output Format:** [Markdown review draft with severity-grouped findings and a confirmation prompt] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May post a GitHub PR review only after explicit user confirmation.] <br>

## Skill Version(s): <br>
0.3.1 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
