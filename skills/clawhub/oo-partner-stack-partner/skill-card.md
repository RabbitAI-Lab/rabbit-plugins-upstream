## Description:

PartnerStack Partner helps agents search and read PartnerStack Partner data through an OOMOL-connected PartnerStack account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve active marketplace programs, partnerships, payouts, and rewards from their connected PartnerStack Partner account through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup tells the agent to run a remote oo CLI installer script that the security summary flags as unverified.

Mitigation: Review the installer before use and prefer installing the oo CLI through verified packages or official documentation you inspect yourself.

Risk: The skill can read PartnerStack partner data such as partnerships, payouts, and rewards through an OOMOL-connected account.

Mitigation: Connect PartnerStack only for accounts where this access is approved, and review requested read actions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-partner-stack-partner)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [PartnerStack Partner homepage](https://partnerstack.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When connector actions are executed, responses are returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
