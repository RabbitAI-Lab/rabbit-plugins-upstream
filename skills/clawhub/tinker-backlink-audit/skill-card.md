## Description:

TinkerClaw Backlink Audit helps agents audit inbound links to a domain, subdomain, or GitHub repo and classify each source as owned, organic, or ambiguous across GitHub referrers, URL lists, backlinks.sh, and Google Search Console CSV exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and growth or SEO maintainers use this skill to collect backlink and referrer inputs, classify which links they control, and produce an audit that separates organic traction from self-created links. It is useful for refreshing inbound-link metrics without treating all backlinks as the same signal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using --source backlinks sends the target domain and backlinks.sh API key to api.backlinks.sh.

Mitigation: Use that source only when the API call is intended; otherwise use offline URL lists, a Google Search Console CSV export, or GitHub referrers.

Risk: The shipped allowlist and historical SERIES are example data from the publisher and can misrepresent another user's backlink ownership or history.

Mitigation: Replace assets/ours-allowlist.json and the build-history SERIES with your own verified domains, URLs, and dated observations before relying on the counts or writing history.

Risk: Optional state-writing commands can update local OpenClaw inbound-link metrics.

Mitigation: Run the tools without --write-state or without build-history.mjs --yes until the exact target key and historical metrics have been reviewed.

Risk: GitHub source data is traffic referrer data rather than raw backlink data.

Mitigation: Treat GitHub results as a repo-scoped traffic proxy and use URL lists, backlinks.sh, or Google Search Console CSVs when raw backlink evidence is needed.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/globalcaos/skills/tinker-backlink-audit)
- [Backlink Sources Reference](references/sources.md)
- [TinkerClaw Repository](https://github.com/globalcaos/tinkerclaw)
- [backlinks.sh](https://backlinks.sh)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; the audit CLI can emit plain text or JSON reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include owned, organic, ambiguous, and total link counts; optional state writes exclude ambiguous links.]

## Skill Version(s):

1.1.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
