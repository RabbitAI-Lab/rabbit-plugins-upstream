## Description:

Tavily helps agents operate Tavily through the OOMOL oo CLI, including web search, crawling, URL mapping, content extraction, usage checks, and asynchronous research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Tavily search, crawl, map, extract, usage, and research actions through an OOMOL-connected Tavily account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the OOMOL CLI, which may be unsafe if an agent runs them automatically or from an unverified source.

Mitigation: Review the installation path first and prefer a verified package, pinned release, checksum, or manually inspected installer before installation.

Risk: The skill can start asynchronous Tavily Research tasks, which may change service state or consume account resources.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Tavily Skill Page](https://clawhub.ai/oomol/skills/oo-tavily)
- [Tavily Homepage](https://tavily.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects that include data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
