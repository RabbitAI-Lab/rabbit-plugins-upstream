## Description:

Manages open source repositories by triaging issues, reviewing code, testing, releasing updates, auditing security, and maintaining documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to coordinate routine public open source repository work, including issue triage, pull request review, testing, release notes, documentation updates, and security review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell commands or file-writing actions may affect the wrong repository if the workspace is not confirmed.

Mitigation: Confirm the intended workspace before use and review proposed commands or file changes before execution.

Risk: Persistent memory may retain secrets or private project details if sensitive content is provided.

Mitigation: Avoid supplying secrets or private project data to memory-backed workflows unless retention is acceptable.

## Reference(s):

- [Open Source Maintainer Team on ClawHub](https://clawhub.ai/t3ratech/skills/oss-maintainer-team)
- [t3ratech publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, code snippets, shell commands, and repository maintenance guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file-writing recommendations, test plans, release notes, documentation updates, and command suggestions for repository maintenance.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
