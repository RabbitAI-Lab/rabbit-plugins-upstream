## Description:

Compare Kickstarter campaigns through Crawlora using funding snapshots, reward tiers, creator updates, risks, and sampled backer comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, creators, and analysts use this skill to compare Kickstarter campaigns for campaign benchmarks, launch research, and evidence-based progress or fulfillment briefs. It helps preserve lifecycle stage, currency, reward, update, and comment sampling limits in the resulting analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an API base chosen through CRAWLORA_API_BASE.

Mitigation: Use the skill in a clean environment, leave CRAWLORA_API_BASE unset unless the destination is fully trusted, and rotate the key if it was used with an untrusted host.

Risk: The bundled helper can call broader Crawlora endpoints than the Kickstarter-focused workflow needs.

Mitigation: Constrain use to the Kickstarter endpoints documented in reference/endpoints.md unless a reviewer approves a broader Crawlora API call.

Risk: Campaign comments and project details may be incomplete snapshots rather than exhaustive evidence.

Mitigation: Report collection bounds, distinguish collected comments from total_count, and avoid inferring delivery outcomes, fraud, or funding velocity from a single snapshot.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Kickstarter project basics](https://help.kickstarter.com/hc/en-us/articles/115005028514-What-are-the-basics)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and cited campaign evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include campaign links, cohort rules, dated funding and reward comparisons, update milestones, sampled comment themes with counts, disagreements, and open questions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
