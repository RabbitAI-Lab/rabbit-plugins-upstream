## Description:

treg helps agents find and call external or live-data APIs for SEO, SERP, backlinks, social trends, enrichment, ads, scraping, and connected account workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superdesigndev](https://clawhub.ai/user/superdesigndev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use treg when an agent needs live data, provider APIs, or connected account actions without asking the human to supply provider keys directly. The skill guides setup, catalog discovery, price review before paid calls, tool invocation, credential sharing, and team administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow uses an external install script and asks for broad command authority around the treg CLI.

Mitigation: Review the install script before running it and approve only the treg commands needed for the task.

Risk: The skill can broker calls to connected tools, accounts, and stored credentials.

Mitigation: Use scoped agent tokens and narrowly selected tools or directories, and confirm the intended organization and account before account-modifying calls.

Risk: Catalog calls can spend the team's prepaid balance.

Mitigation: Read and state the endpoint price before calling, batch-confirm cheap calls when appropriate, and use idempotency keys for genuine retries.

Risk: Server-resolved GitHub provenance is unavailable for this release.

Mitigation: Rely on the ClawHub publisher profile and release evidence for attribution, and verify publisher trust before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/superdesigndev/skills/treg)
- [treg service endpoint](https://treg.to)
- [treg MCP endpoint](https://treg.to/mcp/)
- [treg agent onboarding](https://treg.to/llms.txt)
- [treg tutorial](https://treg.to/tutorial)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to call paid catalog endpoints or registered tools after price review and user confirmation.]

## Skill Version(s):

0.11.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
