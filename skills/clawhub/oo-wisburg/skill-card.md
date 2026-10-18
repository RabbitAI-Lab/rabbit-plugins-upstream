## Description:

Helps agents search and read Wisburg research, articles, news, and market updates through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents serving Wisburg users can find and read research reports, articles, earnings-call minutes, news feeds, and market updates from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running a remotely fetched installer script directly in a shell.

Mitigation: Review the installer or use a verified, pinned package with checksum or signature validation before installing the CLI.

Risk: Broad routing of Wisburg requests and connected-account access could expose account data through the OOMOL service.

Mitigation: Use only for intended Wisburg tasks and connect the account only if OOMOL-mediated access is acceptable.

## Reference(s):

- [Wisburg](https://www.wisburg.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Wisburg skill release](https://clawhub.ai/oomol/skills/oo-wisburg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown responses with Wisburg content or suggested CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content and available fields vary by Wisburg action.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
