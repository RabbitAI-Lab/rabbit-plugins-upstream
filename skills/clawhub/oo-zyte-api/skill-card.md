## Description:

Zyte API connector that lets an agent extract article, page, product, and browser-rendered HTML data from public URLs through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Zyte API read actions for extracting structured content and rendered HTML from public URLs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute unverified remote installer scripts on the user's machine.

Mitigation: Install the oo CLI manually from a trusted, version-pinned source, verify any installer before running it, and do not let an agent execute curl|bash or irm|iex setup commands automatically.

## Reference(s):

- [Zyte API homepage](https://www.zyte.com/zyte-api/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zyte-api)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
