## Description:

Screens startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Buyers and acquisition researchers use this skill to shortlist startups for sale, compare asking prices and dated revenue histories, and identify open diligence questions. It supports research, not an investment recommendation or transaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Startup queries, public URLs, and scrape parameters are sent to Crawlora along with the API key.

Mitigation: Keep the key in the environment and omit private buyer constraints, internal URLs, and notes unless intentionally sharing them with Crawlora.

Risk: Broad research can incur API costs or conflict with website terms.

Mitigation: Check API costs and website terms before broad scraping; bound searches to the buyer's brief.

Risk: Verified revenue and seller asking prices do not establish profit, transferable ownership, or investment value.

Mitigation: Label metric dates and definitions, separate seller claims from verified figures, and seek independent diligence before making decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/startup-acquisition-research)
- [Crawlora](https://crawlora.net)
- [TrustMRR FAQ](https://trustmrr.com/faq)
- [Skill endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown candidate table and diligence questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, dated metrics, defined calculations, history coverage, discrepancies, and open questions.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
