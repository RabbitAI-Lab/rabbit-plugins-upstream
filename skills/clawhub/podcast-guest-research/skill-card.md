## Description:

Find podcasts suited to a proposed guest using Crawlora's podcast catalog, live show and episode data, and public show websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research podcast guest opportunities, build sourced show shortlists, inspect recent episode fit, and draft pitch angles while preserving caveats about audience size, booking availability, and accepted submission channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can send the Crawlora API key and arbitrary requests beyond the documented podcast workflow.

Mitigation: Review before installing, use only a Crawlora key suitable for this workflow, and prefer restricting helper usage to the documented podcast and web-scrape endpoints.

Risk: Sensitive private material could be submitted as scrape input or POST data.

Mitigation: Do not pass sensitive private material to the scrape or POST inputs, and review request bodies before execution.

Risk: Changing CRAWLORA_API_BASE can redirect the API key and request data to an untrusted destination.

Mitigation: Avoid setting CRAWLORA_API_BASE unless the destination is fully trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/podcast-guest-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with sourced shortlist entries and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include show and host names, canonical links and IDs, fit rationale, recent episode evidence with dates, proposed pitch angles, verified submission channels, and caveats.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
