## Description:

GitHub Flow guides agents through GitHub issue and pull request workflows including planning, PR creation, review, dependency tracking, sanitization, publishing, and guarded merges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to prepare GitHub issues and pull requests, coordinate review feedback, manage issue dependencies, sanitize public-facing text, and execute guarded PR publication or merge workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to perform broad GitHub write operations through local gh authentication, including issue and PR edits, reviewer requests, account switching, and merges.

Mitigation: Install only for agents authorized to operate on the target repositories, keep gh authentication scoped to the needed accounts, and require user review before write, account-switch, push, ready-transition, or merge actions.

Risk: Server security guidance reports inconsistent draft-to-ready PR instructions in the artifact.

Mitigation: Review and standardize the draft-to-ready approval rule before deployment; until then, require explicit user approval before transitioning a draft PR to ready.

Risk: GitHub issue, PR, comment, review, and merge text can expose personal data or local workflow artifact paths when posted to public repositories.

Mitigation: Apply the documented sanitize checks before posting public-facing GitHub text, including scans for personal data and internal artifact paths.

Risk: The PR URL gate script is present, but the skill documentation says it is not currently registered in a hook configuration.

Mitigation: Treat the gate as advisory unless hook registration is verified, and manually include full clickable URLs for PR or issue references in decision prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and GitHub CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include issue bodies, PR bodies, review comments, checklists, command sequences, and workflow decisions for GitHub operations.]

## Skill Version(s):

0.10.0 (source: server release metadata and changelog, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
