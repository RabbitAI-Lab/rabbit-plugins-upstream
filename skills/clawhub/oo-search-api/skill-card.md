## Description:

SearchApi (searchapi.io) lets an agent search, retrieve cached SearchApi results, look up canonical locations, and inspect SearchApi account usage through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate SearchApi through OOMOL's connector instead of handling API calls or raw credentials directly. It supports web search, cached result retrieval in HTML or JSON, location lookup for geo-targeted queries, and account usage checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Before installation, prefer official package-manager or versioned release instructions when available and verify checksums or signatures where provided; do not run remote installer commands automatically in sensitive workspaces.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-search-api)
- [SearchApi Homepage](https://www.searchapi.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before constructing connector requests.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
