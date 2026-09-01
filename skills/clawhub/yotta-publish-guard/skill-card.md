## Description:

元守 yotta-publish-guard helps developers run pre-publish checks, package validation, version alignment, name availability checks, and dry-run or explicit publish command plans for agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and release maintainers use this skill before publishing or updating agent skills across GitHub, npm, and ClawHub. It helps review readiness, package contents, version consistency, name availability, and generated publish command plans while leaving the final release decision to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated publish command plans can affect external release channels when explicitly executed.

Mitigation: Review the generated commands before using --exec, and use the default dry-run output until the release plan is confirmed.

Risk: Using --force can bypass the normal push gate.

Mitigation: Reserve --force for cases where a human has reviewed and accepted the blocked condition.

Risk: Broad installation can make the skill available to agents beyond the intended release workflow.

Mitigation: Install only into the agent skill directory where this release guard should be available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [GitHub repository](https://github.com/YottaMeta/yotta-publish-guard)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-publish-guard)
- [Check Items](references/check-items.md)
- [Publish Flow](references/publish-flow.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured readiness findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publish actions are dry-run by default; execution requires explicit flags.]

## Skill Version(s):

0.2.0 (source: frontmatter, package.json, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
