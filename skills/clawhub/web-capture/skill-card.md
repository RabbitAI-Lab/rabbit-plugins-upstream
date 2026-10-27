## Description:

Monitors company and competitor web pages and news weekly, then proposes evidence-tagged updates to company context in a pull request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, revenue operations, and GTM engineering teams use this skill to track changes to company and competitor pages and news, seed company context, and review weekly updates before merging them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scheduled agent consumes untrusted web content and can create repository branches and pull requests.

Mitigation: Restrict repository paths and commands, require human review of generated context before merging, and inspect the plan before deployment.

Risk: The agent may target an unintended repository or run with an unpinned CLI version.

Mitigation: Confirm the resolved GitHub repository binding and pin the Cargo CLI version before enabling the weekly schedule.

## Reference(s):

- [ClawHub release](https://clawhub.ai/cargo-ai/skills/web-capture)
- [Project homepage listed in skill metadata](https://github.com/getcargohq/gtm-skills)
- [Skill homepage listed in frontmatter](https://github.com/getcargohq/gtm-skills/tree/main/web-capture)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Text]

**Output Format:** [Markdown context notes and raw page captures, JSON news records, and a pull request for review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [After the initial run, adds dated findings without editing existing context files; a quiet week opens no pull request.]

## Skill Version(s):

0.1.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
