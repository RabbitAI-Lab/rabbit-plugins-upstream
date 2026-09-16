## Description:

Vet public TikTok creators through live profile, post, video, comment, and user-search endpoints in Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build evidence-backed TikTok creator shortlists, refresh public profile and post data, and rank candidates against stated campaign or research criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok request parameters and the Crawlora API key to Crawlora.

Mitigation: Install only if that data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and avoid logging the key.

Risk: Creator profiles, posts, and comments are sampled public-data evidence and may be incomplete or misleading if treated as proof of demographics, authenticity, or partnership quality.

Mitigation: State sample sizes, refresh times, formulas, and unknowns; avoid unsupported claims about audience demographics, authenticity, or conversion potential.

## Reference(s):

- [tiktok-creator-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-creator-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured shortlist fields and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bounded public TikTok profile, post, detail, and comment samples; requires CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
