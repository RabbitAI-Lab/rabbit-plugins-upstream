## Description:

Guides agents in using Firecrawl through an OOMOL-connected account to scrape, crawl, search, and extract website content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Firecrawl users can guide an agent to scrape, crawl, search, map, and extract web content, manage jobs, and check usage through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions suggest running a remote CLI installer that has not been verified in the supplied security assessment.

Mitigation: Review the setup path and use verified official installation documentation; do not allow an agent to run the remote installer automatically without trusting its source.

Risk: Firecrawl actions can change account state or cancel jobs.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval for destructive actions.

## Reference(s):

- [Firecrawl skill listing](https://clawhub.ai/oomol/skills/oo-firecrawl)
- [Firecrawl](https://www.firecrawl.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with shell commands and Firecrawl results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested Firecrawl action and connected account.]

## Skill Version(s):

1.0.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
