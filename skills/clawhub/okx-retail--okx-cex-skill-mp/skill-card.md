## Description:

Browse, search, install, download, update, remove, and verify AI trading skills in the OKX Skills Marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

External users of the OKX CLI use this skill to find marketplace skills and manage local installs, downloads, updates, removals, and signature checks. Marketplace access requires configured API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented installer uses an unpinned `npx skills` dependency, and the security scan had partial coverage.

Mitigation: Delay installation until the dependency is pinned and scan coverage is resolved. If proceeding, verify the installer source and version, and review what the `--force` option bypasses.

## Reference(s):

- [OKX website](https://www.okx.com)
- [ClawHub skill listing](https://clawhub.ai/okx-retail/skills/okx-cex-skill-mp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown with CLI examples and command tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the OKX CLI and API credentials for marketplace access.]

## Skill Version(s):

1.5.1 (source: frontmatter and server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
