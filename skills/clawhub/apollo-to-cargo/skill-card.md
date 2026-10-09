## Description:

Helps revenue operations teams rebuild a sample Apollo list in Cargo and compare verified contact coverage and credit costs before migrating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and go-to-market teams can sample an Apollo export, enrich the same records through Apollo and Cargo, and compare verified hit rates and credits spent before approving a full-list run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enrichment calls consume Cargo credits, and a full-list run can scale costs quickly.

Mitigation: Start with 10–20 records, report actual credit use and estimated full-list cost, and get approval before expanding the run.

Risk: The setup installs the latest Cargo CLI package without pinning a version.

Mitigation: Review the package and its source before installing in sensitive environments; pin a reviewed version when appropriate.

Risk: The skill can record a session in Cargo and leave local agent-state markers.

Mitigation: Review the session and local-state steps before running the workflow.

Risk: An optional GitHub star request is unrelated to comparing contact data and may use the user's GitHub identity.

Mitigation: Decline or ignore the request if unwanted; never star without explicit user consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/apollo-to-cargo)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Apollo provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/apolloio.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands]

**Output Format:** [Markdown with a comparison table and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports verified hit rate, credits spent, and credits per verified record for each source on the same sampled rows.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
