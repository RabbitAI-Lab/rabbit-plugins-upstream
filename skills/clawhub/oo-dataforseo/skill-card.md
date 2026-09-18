## Description:

DataForSEO enables agents to read, create, and update DataForSEO data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate DataForSEO through an OOMOL-connected account for SEO, SERP, backlink, keyword, competitor, domain ranking, and Amazon Merchant API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include a remote installer that could run arbitrary code if its source is compromised.

Mitigation: Review the setup path before installing; prefer a trusted, versioned oo CLI source with checksum or signature verification.

Risk: Write actions can create paid DataForSEO tasks or change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [DataForSEO homepage](https://dataforseo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
