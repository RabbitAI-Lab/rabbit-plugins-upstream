## Description:

Hyperbrowser lets an agent fetch pages, search the web, retrieve crawl results, check crawl status, and start Hyperbrowser crawl jobs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Hyperbrowser through OOMOL for web search, page fetching, and crawl workflows while relying on live connector schemas for action payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer one-liners executed directly in a shell.

Mitigation: Prefer a verified package, pinned release, checksum or signature validation, or inspect the downloaded installer before execution.

Risk: The start_web_crawl action changes Hyperbrowser account state.

Mitigation: Confirm the exact crawl payload and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hyperbrowser)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Hyperbrowser Homepage](https://www.hyperbrowser.ai)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Hyperbrowser Connection](https://console.oomol.com/app-connections?provider=hyperbrowser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results are returned as JSON when the agent executes the documented commands.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
