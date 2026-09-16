## Description:

Spider Cloud helps an agent search the web, scrape public URLs, extract links, and check account credits through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Spider Cloud read actions for web search, scraping, link extraction, and account credit checks through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that execute downloaded shell or PowerShell content.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI through a verified package, pinned release, checksum, or signed installer before using the skill.

## Reference(s):

- [Spider Cloud ClawHub Skill](https://clawhub.ai/oomol/skills/oo-spider)
- [Spider Cloud Homepage](https://spider.cloud)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected Spider Cloud account; connector responses include data and an execution id.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
