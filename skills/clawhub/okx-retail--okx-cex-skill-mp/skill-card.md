## Description:

Helps agents discover, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-assistant users can search the OKX Skills Marketplace, manage locally installed skills, and check their signatures before use. Marketplace access requires OKX API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace skills from third parties can change agent behavior and access local permissions after installation.

Mitigation: Review each skill and its publisher before installation, and check where it will be installed across local agents.

Risk: Force installation bypasses signature verification.

Mitigation: Avoid --force unless the package has been deliberately audited; verify installed skills before use.

Risk: An unpinned installer can fetch a different CLI version than the reviewed release.

Mitigation: Prefer a pinned or trusted installer version, such as @okx_ai/okx-trade-cli@1.4.9.

## Reference(s):

- [OKX Skills Marketplace release](https://clawhub.ai/okx-retail/skills/okx-cex-skill-mp)
- [OKX](https://www.okx.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Marketplace search results, installation status, and signature-verification results may be shown as text or JSON.]

## Skill Version(s):

1.4.9 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
