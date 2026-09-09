## Description:

GitHub market recon when the user asks for AI money trends, hot niches, competitor signals, or "找风口/赚钱方向调研", especially when sources are restricted to GitHub only or a previous research run was interrupted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xianxing475](https://clawhub.ai/user/xianxing475)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, builders, and market researchers use this skill to produce evidence-linked GitHub trend and opportunity reports for AI money trends, hot niches, competitor signals, and monetization-oriented research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub API throttling or truncated responses can leave market evidence incomplete.

Mitigation: Use capped batches, switch to GitHub HTML search on throttling, disclose interruptions, and fetch single-repo metadata before quoting repository statistics.

Risk: GitHub popularity may be mistaken for revenue validation.

Mitigation: State that GitHub heat indicates tool or content demand rather than proven revenue, and link each trend conclusion to fetched GitHub evidence.

Risk: Research scope could expand beyond the intended source boundary.

Mitigation: Keep fetches limited to github.com and api.github.com, avoid file writes, and verify that the final report contains no non-GitHub sources.

## Reference(s):

- [Proven URL Sets for GitHub Recon](references/url-sets.md)
- [ClawHub Skill Page](https://clawhub.ai/xianxing475/skills/market-recon)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report in chat with evidence links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Every substantive claim should trace to fetched GitHub evidence; no user files are written.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
