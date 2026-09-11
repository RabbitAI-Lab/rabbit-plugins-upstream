## Description:

YuanShou yotta-publish-guard helps developers and release teams run pre-publish checks, package validation, version alignment, name availability checks, and dry-run or explicit release command planning for agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and release engineers use this skill before publishing or updating agent skills to check release readiness, validate package contents, align versions, check name availability, and prepare guarded publish commands. It supports GitHub, npm, and ClawHub-oriented release workflows while leaving final publish decisions and credentials with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package inspection and executable publish paths can run local project code.

Mitigation: Run the skill only on trusted skill directories, pin the npm version when installing, and review command plans before using --exec.

Risk: Publish commands can upload broad directory contents to public channels.

Mitigation: Review the exact files to be published, run a secret scan before execution, and keep the default dry-run flow until the release contents are confirmed.

Risk: Automatic target detection can point installation or checks at an unintended location.

Mitigation: Prefer explicit --agent or --dir arguments instead of relying on global or auto-detected installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [Publisher profile](https://clawhub.ai/user/yottameta)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-publish-guard)
- [GitHub repository](https://github.com/YottaMeta/yotta-publish-guard)
- [check-items](references/check-items.md)
- [publish-flow](references/publish-flow.md)
- [tutorial](references/tutorial.md)
- [faq](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text]

**Output Format:** [Markdown and text with inline shell commands and release check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run publish plans, readiness verdicts, version alignment reports, package inspection summaries, and manual follow-up prompts when network checks are unavailable.]

## Skill Version(s):

0.3.0 (source: frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
