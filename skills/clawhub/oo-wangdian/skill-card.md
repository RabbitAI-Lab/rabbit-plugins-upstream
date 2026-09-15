## Description:

Wangdian ERP (wangdian.cn) skill for searching and reading Wangdian ERP data through the OOMOL-connected wangdian connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect schemas and read Wangdian ERP records such as goods, inventory, orders, refunds, stockouts, shops, and warehouses through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified remote installer commands could execute changing code on a user's machine.

Mitigation: Review the oo CLI installation path before installing and prefer a pinned, signed, or package-manager installation method instead of running curl | bash or irm | iex.

Risk: Connecting Wangdian ERP through OOMOL-mediated read access can expose ERP business records available to the connected account.

Mitigation: Connect only the intended Wangdian ERP account and scopes, and confirm the user is comfortable with OOMOL-mediated read access to the listed data.

## Reference(s):

- [Wangdian ERP homepage](https://www.wangdian.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wangdian)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide live schema inspection before constructing oo CLI connector requests.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
