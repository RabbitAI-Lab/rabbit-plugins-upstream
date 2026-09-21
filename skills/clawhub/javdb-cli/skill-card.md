## Description:

Operates the javdb CLI to search JavDB records, retrieve details, navigate lists and rankings, and perform account or watch-state changes only after explicit user authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they explicitly want an agent to operate an installed javdb-cli binary for JavDB search, navigation, authenticated account checks, preview asset saves, or confirmed account state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can contact JavDB or App API services and may upload user-approved images for reverse search.

Mitigation: Run networked or image-upload workflows only when the user explicitly requests them, and explain the privacy impact before reverse image search.

Risk: Saved account state can include credentials and JWTs.

Mitigation: Do not read or disclose the local auth file; use only the CLI account commands documented by the skill and never echo passwords or tokens.

Risk: Account, configuration, and watch-state commands can change local or remote state.

Mitigation: Require explicit per-operation authorization and confirm the target item, account, configuration key, or state change before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flanchanxwo/skills/javdb-cli)
- [Project homepage](https://github.com/FlanChanXwO/javdb-cli)
- [Authentication and accounts](references/auth.md)
- [Search and navigation workflows](references/discover.md)
- [Installation and version checks](references/install.md)
- [State-changing operations](references/state.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON or NDJSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local preview asset files only after explicit user approval; does not produce full media downloads.]

## Skill Version(s):

0.8.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
