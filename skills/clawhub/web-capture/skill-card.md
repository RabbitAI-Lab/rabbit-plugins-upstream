## Description:

Keeps company context current by reviewing company and competitor web pages and news weekly, then proposing sourced updates in a pull request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM engineers, RevOps teams, and marketers use this skill to seed company context from public web sources and propose weekly updates about their company and competitors for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unattended agent reads untrusted web content and can run commands and write to its repository.

Mitigation: Run initial captures manually, restrict GitHub access to the intended repository, and review pull requests for unexpected files or prompt-injection artifacts before merging.

Risk: The fallback installation uses an unpinned Cargo CLI version.

Mitigation: Pin the Cargo CLI version before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/web-capture)
- [Skill homepage listed in metadata](https://github.com/getcargohq/gtm-skills/tree/main/web-capture)
- [Project homepage listed in ClawHub metadata](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Markdown, Text, Configuration guidance, Shell commands]

**Output Format:** [Markdown guidance and commands for a scheduled agent that proposes sourced context files in a pull request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public-source claims are tagged by evidence level; changes require pull-request review.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
