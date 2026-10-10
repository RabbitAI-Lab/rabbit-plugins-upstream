## Description:

Maps podcast topics across sampled public Apple Podcasts and Spotify shows and episodes to support editorial comparisons and listening shortlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Podcast editors, researchers, and creators compare topic coverage across selected public shows and episodes and assemble an evidence-linked listening shortlist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast search terms, IDs, and query parameters are sent to Crawlora using a user-provided API key.

Mitigation: Only supply a key if comfortable with the service, keep it private, and limit queries to intended public podcast metadata.

Risk: Sampled descriptions may not reflect spoken content or the full podcast catalog.

Mitigation: Keep source links and sampling limits visible; verify content independently before attributing statements or drawing broad conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/podcast-topic-landscape)
- [Podcast endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Show-by-topic matrix, dated episode evidence ledger, and listening shortlist; conclusions are limited to sampled public metadata.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
