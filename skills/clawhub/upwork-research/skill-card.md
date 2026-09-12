## Description:

Researches Upwork job postings and freelancer profiles via the Crawlora API, returning normalized JSON for job search, job detail, freelancer profile, market-rate research, and freelancer vetting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and business users use this skill to search public Upwork job listings, inspect job details, and research freelancer profiles through Crawlora before market-rate analysis, hiring outreach, or freelancer vetting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Upwork search terms, public job or freelancer IDs, and the Crawlora API key are sent to Crawlora.

Mitigation: Install only if that disclosure is acceptable, keep the key in the environment, and review Crawlora and Upwork terms for the intended use.

Risk: The API key could be exposed if it is hardcoded, committed, or passed through unsafe command arguments.

Mitigation: Use CRAWLORA_API_KEY as instructed; the helper keeps the key out of normal command arguments and validates the key format before use.

Risk: Public Upwork data can change and may be incomplete for high-stakes hiring or pricing decisions.

Mitigation: Treat returned JSON as research input and verify important decisions against current public Upwork postings or profiles.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/upwork-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with optional Markdown explanations and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses the documented Upwork endpoints exposed by Crawlora.]

## Skill Version(s):

1.0.14 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
