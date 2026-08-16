## Description:

LeadBoxer helps agents enrich domains and IP addresses through an OOMOL-connected LeadBoxer account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs LeadBoxer domain or IP enrichment for organization, firmographic, network, or geolocation data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain or IP lookup inputs are sent through the OOMOL LeadBoxer connector.

Mitigation: Use the skill only for intended LeadBoxer enrichment tasks and confirm sensitive or ambiguous lookup targets before running an external lookup.

Risk: Connector payload requirements may change over time.

Mitigation: Inspect the live LeadBoxer action schema before building each JSON payload.

## Reference(s):

- [LeadBoxer homepage](https://www.leadboxer.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are returned as JSON when the agent runs LeadBoxer lookups.]

## Skill Version(s):

1.0.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
