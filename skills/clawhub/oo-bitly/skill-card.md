## Description:

Bitly (bitly.com). Use this skill for Bitly requests that read, create, or update Bitly data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to inspect Bitly account data, create short links, and update editable Bitlink fields through the OOMOL Bitly connector. It is intended for intentional Bitly account work where state-changing payloads are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents remote installer commands for the OOMOL CLI.

Mitigation: Install the CLI only from a source you independently trust and verify; prefer a preinstalled or managed CLI where available.

Risk: The skill can create short links and update Bitly Bitlinks.

Mitigation: Use it only for intentional Bitly account work, fetch the live connector schema first, and confirm every shorten or update payload before running it.

Risk: The routing language is broader than necessary for Bitly requests.

Mitigation: Limit use to Bitly-specific tasks and avoid applying the skill to unrelated URL management or analytics work.

## Reference(s):

- [ClawHub Bitly skill page](https://clawhub.ai/oomol/skills/oo-bitly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Bitly homepage](https://bitly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
