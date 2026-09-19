## Description:

Firecrawl lets an agent use an OOMOL-connected Firecrawl account to scrape, search, crawl, extract, monitor jobs, generate LLMs.txt output, and manage Firecrawl jobs through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Firecrawl through an OOMOL-connected account for web scraping, search, crawling, extraction, usage monitoring, and job management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute changing code on the user's machine.

Mitigation: Review the setup path before installation and prefer a verified, pinned, or package-manager-based oo CLI install method.

Risk: Firecrawl write or destructive actions can change or cancel remote jobs and data.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before write actions; require explicit approval for destructive actions.

Risk: Successful execution depends on an authenticated OOMOL account, a connected Firecrawl credential, and available billing credits.

Mitigation: Run setup or account-repair steps only after matching auth, connection, credential, or billing errors, and verify the account state before retrying.

## Reference(s):

- [Firecrawl homepage](https://www.firecrawl.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-firecrawl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Firecrawl action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
