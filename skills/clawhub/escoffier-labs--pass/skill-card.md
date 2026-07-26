## Description: <br>
Use before opening a pull request, before running gh pr create, or before pushing follow-up commits to an existing PR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[escoffier-labs](https://clawhub.ai/user/escoffier-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to check whether a pull request is ready to file or update. It guides review of root-cause fixes, tests, scope, diffs, artifact cleanliness, PR body quality, and existing PR state before public GitHub actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to run a stricter checklist before opening or updating pull requests, which can delay PR filing when checks fail. <br>
Mitigation: Use it before public GitHub actions and expect failed checklist items to be surfaced, fixed, and re-run before filing. <br>
Risk: The skill may advise shell commands such as checking PR state with gh before pushing follow-up commits. <br>
Mitigation: Review proposed commands and PR body text before execution or publication, especially for repositories outside the user's ownership. <br>
Risk: The artifact emphasizes artifact cleanliness because public PRs can accidentally expose secrets, internal hostnames, private IPs, or private context. <br>
Mitigation: Scan the diff, branch name, commit messages, and PR body for sensitive or identifying content before opening or updating the PR. <br>


## Reference(s): <br>
- [Pass on ClawHub](https://clawhub.ai/escoffier-labs/pass) <br>
- [Escoffier Labs publisher profile](https://clawhub.ai/user/escoffier-labs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with checklist items and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May draft PR body text, recommend checks to run, and advise whether PR creation or follow-up commits should proceed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
