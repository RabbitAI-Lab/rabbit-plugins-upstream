## Description:

Researches public local-business profiles, ratings, reviews, complaints, scam reports, menus, and photos across Yelp, BBB, Trustpilot, and OpenTable using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Business researchers, procurement teams, and agents use this skill to compare public reputation signals for local businesses or restaurants while keeping source boundaries, identity matches, and review evidence explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business names, locations, domains, and other search identifiers are sent to Crawlora and may reveal vendor due-diligence targets.

Mitigation: Use only public business research inputs, avoid private customer records or sensitive internal notes, and provide explicit country or locale values when researching non-US businesses.

Risk: Ratings, reviews, complaints, and scam reports are platform-reported records and may be incomplete, moderated, duplicated, or attached to the wrong branch.

Mitigation: Preserve source URLs or IDs, platform names, collection time, and unresolved identity matches; avoid drawing fraud, safety, or service-quality conclusions from a single review or rating.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/local-business-reputation-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reputation brief with linked evidence and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific ratings, review themes, complaints, scam-report references, menu details, photos, source URLs or IDs, and collection time.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
