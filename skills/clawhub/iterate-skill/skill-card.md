## Description:

Automates multi-round code review and fixes, with a defensive workflow for incremental programming tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use Iterate to review a project across multiple quality dimensions, fix issues over successive rounds, or implement incremental changes with defensive checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project configuration may cause untrusted commands to run during checks.

Mitigation: Review iterate.config.yaml and validation.commands before running guard, post-check, or invariant workflows; use only in repositories where project test and build commands are acceptable.

Risk: Automated changes may be merged or published if those options are enabled.

Mitigation: Keep automatic merge and push disabled unless publication is explicitly intended, and review the proposed changes first.

Risk: Installing or updating the skill in a sensitive repository may introduce unreviewed code.

Mitigation: Review the skill before installation and prefer the checksum-verified installer or update path.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Code changes and Markdown review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can modify project files and run project checks; automatic merge and push are disabled by default.]

## Skill Version(s):

3.5.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
