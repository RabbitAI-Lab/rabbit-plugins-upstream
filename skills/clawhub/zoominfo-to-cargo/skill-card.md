## Description:

Rebuilds a ZoomInfo, Lusha, or Cognism contact-list sample in Cargo so teams can compare verified coverage and estimated credits before renewal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM operators, sales operations teams, and developers use this skill to sample an incumbent contact-list export, re-enrich the same records through Cargo, verify both sides, and compare verified coverage and credit cost before a database renewal decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business contact and company records may be sent to Cargo for enrichment and verification.

Mitigation: Install and run the skill only when the user is comfortable sharing sampled business records with Cargo, and start with the documented 10-20 row sample before any larger run.

Risk: The skill includes under-disclosed vendor session attribution.

Mitigation: Review the session attribution command before setup and skip it when the user does not want Cargo to record the skill session.

Risk: The skill includes an unrelated GitHub starring action that could endorse a repository from the user's authenticated GitHub account.

Mitigation: Run the GitHub star command only after the user explicitly agrees; otherwise omit it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/zoominfo-to-cargo)
- [Cargo GTM Skills Repository](https://github.com/getcargohq/gtm-skills)
- [Cargo Waterfall Provider Playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, configuration]

**Output Format:** [Markdown with inline bash commands and reporting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides sampled enrichment and verification workflows that may call Cargo services through the Cargo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
