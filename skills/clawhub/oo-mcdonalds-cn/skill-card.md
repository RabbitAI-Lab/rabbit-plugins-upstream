## Description:

McDonald's China lets agents search and read supported city, store, business, menu, product, and product detail data through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query McDonald's China locations, menus, product details, and store business information from an OOMOL-connected account.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The fallback setup path tells users to execute an unpinned remote installer directly in a shell.

Mitigation: Prefer an independently verified oo CLI installation method, review the installer source before execution, and avoid running installer commands unless the CLI is actually missing.

Risk: The skill depends on an OOMOL-connected account and server-side credentials for McDonald's China queries.

Mitigation: Review account connection, billing, and credential-scope steps before use, and run connection or authentication setup only after a command reports a matching failure.

## Reference(s):

- [McDonald's China homepage](https://open.mcd.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mcdonalds-cn)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns read-only McDonald's China data when the user's OOMOL account is connected.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
