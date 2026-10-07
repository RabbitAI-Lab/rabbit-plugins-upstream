## Description:

Checks skill releases for publishing readiness, package contents, version alignment, and name availability, then prepares or executes publishing commands on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release teams use this skill to check agent-skill packages before publishing to GitHub, npm, or ClawHub and to review a dry-run publishing plan before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Executing a publishing plan can create or push repositories and publish packages using locally authenticated CLIs.

Mitigation: Review the dry-run plan, destination ownership, and release contents before explicitly using --exec.

Risk: A publishing gate can be bypassed with --force, and network outages can prevent name checks.

Mitigation: Avoid bypassing the gate without manual review and confirm name availability when network checks are unavailable.

Risk: Unpinned npx installs can fetch a newer package than the version reviewed.

Mitigation: Pin the package version when installing through npx.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [Project homepage](https://github.com/YottaMeta/yotta-publish-guard)
- [Publishing checklist](references/check-items.md)
- [Publishing flow](references/publish-flow.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes readiness results and a dry-run publishing plan by default.]

## Skill Version(s):

0.4.3 (source: frontmatter, CHANGELOG, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
