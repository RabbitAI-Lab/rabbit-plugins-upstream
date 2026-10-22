## Description:

Research recent crypto-market developments from free public sources, verify original evidence, deduplicate stories, and track changes to a local watchlist. Use for crypto intelligence briefs, project updates, event calendars, narrative research and rumor verification; no paid data provider or API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto researchers, analysts, and project teams use this skill to produce source-linked market briefs, project updates, event calendars, and narrative or rumor research. It can also track changes in a local watchlist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-source research may be incomplete or misrepresent an event if claims, timing, or evidence stages are conflated.

Mitigation: Read and link original sources, distinguish announced, proposed, scheduled, and executed events, label uncertainty, and disclose coverage gaps.

Risk: Optional local history and watchlist files, including backups, remain on disk until removed; an incorrect output path could replace a file.

Mitigation: Use a dedicated research folder, preview history changes before committing, review output paths before replacing a watchlist, and remove retained history when no longer needed.

## Reference(s):

- [Research method](artifact/references/research-method.md)
- [Local event contract and incremental state](artifact/references/data-contract.md)
- [Starter source directory](artifact/references/sources.json)
- [Client and installation notes](artifact/references/client-setup.md)
- [MochiPay publisher site](https://mochi.bz/)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Source-linked Markdown briefs; optional JSON research records, watchlists, and event-history files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language, scope, and detail follow the request; current reports should state a UTC cutoff and cite sources. Local history is optional.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; scripts/intel.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
