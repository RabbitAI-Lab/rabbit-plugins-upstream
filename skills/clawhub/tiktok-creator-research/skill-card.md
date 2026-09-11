## Description:

Vets public TikTok creators through Crawlora live profile, post, video, comment, and user-search endpoints for TikTok-only creator research and shortlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and research teams use this skill to build current TikTok creator shortlists from public profile, content, and comment evidence while preserving sampling limits and unknowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok research queries, request bodies, and the Crawlora API key are sent to Crawlora.

Mitigation: Use a scoped Crawlora key, keep it in CRAWLORA_API_KEY, and install only when that data sharing is acceptable.

Risk: An untrusted curl configuration could alter request behavior around a credentialed API call.

Mitigation: Run the helper in a trusted shell environment and avoid inherited or untrusted curl configuration.

Risk: Incorrect endpoint paths could send requests outside the intended TikTok creator-research workflow.

Mitigation: Review the requested endpoint path before execution and keep calls within the documented TikTok route set.

Risk: Public TikTok profile, post, and comment data can be incomplete, sampled, stale, or misinterpreted as demographic or authenticity proof.

Mitigation: Refresh profiles before use, record sample sizes and dates, disclose unknowns, and avoid unsupported claims about audience demographics, authenticity, or partnership history.

## Reference(s):

- [TikTok endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-creator-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise analysis, shortlist tables, metric definitions, unknowns, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include profile URLs, stable creator ids, refresh times, sampled video URLs, engagement formulas, and disclosed discovery or sampling limits.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
