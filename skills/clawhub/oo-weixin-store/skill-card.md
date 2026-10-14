## Description:

Helps agents manage products, orders, fulfillment, and after-sale requests in a connected WeChat Store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators and their agents use this skill to inspect and manage a connected WeChat Store's catalog, orders, shipping, and after-sale requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested first-time setup can run a remote installer on the user's machine.

Mitigation: Review the installer before running it; prefer an official signed or package-manager installation when available.

Risk: Store changes, including product deletion, stock updates, shipping, and after-sale decisions, can be consequential or irreversible.

Mitigation: Confirm the exact target, payload, and effect with the user before any write or destructive action.

## Reference(s):

- [WeChat Store skill listing](https://clawhub.ai/oomol/skills/oo-weixin-store)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [WeChat Store](https://channels.weixin.qq.com/shop)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with store information and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may read or change a connected store.]

## Skill Version(s):

1.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
