## Description:

Compare companies or products using Crawlora website extraction, traffic estimates, reviews, product listings, and hiring data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Business, product, marketing, and strategy users use this skill to prepare competitor briefs, positioning and pricing comparisons, and evidence-backed battlecards. The skill helps agents separate company claims, third-party observations, and interpretation while preserving source links and unknowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected URLs, search terms, comparison criteria, and request bodies are sent to Crawlora with the user's Crawlora API key.

Mitigation: Keep the API key in the environment, review generated requests before running them, and avoid submitting sensitive or unnecessary information.

Risk: Traffic estimates, reviews, product rankings, and job listings can be stale, sampled, incomplete, or unsuitable for direct comparison.

Mitigation: Preserve source URLs, dates, retrieval times, and evidence type; verify disputed or high-impact claims against primary sources; retain disagreements and unknowns.

Risk: Recurring tracking or distribution could broaden collection or sharing beyond a one-time brief.

Mitigation: Treat the default workflow as one-time analysis and set up recurring tracking or distribution only when explicitly requested.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/competitor-intelligence)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief or comparison matrix with sourced claims, plus optional shell commands that return JSON from Crawlora.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a claim ledger, source URLs, retrieval times, supported advantages, gaps, and remaining questions.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
