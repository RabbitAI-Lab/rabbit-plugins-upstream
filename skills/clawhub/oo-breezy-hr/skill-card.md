## Description:

Breezy HR (breezy.hr) helps an agent search and read Breezy HR data through OOMOL's connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting and HR operators use this skill to retrieve Breezy HR companies, positions, candidates, position candidate lists, company-wide candidate email search results, and the current authenticated user profile. It is intended for read-oriented Breezy HR requests where the agent should inspect the live action schema before running connector commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include direct execution of remote installer scripts.

Mitigation: Install the oo CLI only from a trusted OOMOL distribution channel, and prefer downloading, inspecting, and verifying the installer or using a signed/package-managed method before execution.

Risk: The skill can access recruiting records from Breezy HR through the connected account.

Mitigation: Use accounts with appropriate Breezy HR permissions and inspect each live action schema before sending company, position, candidate, or email search payloads.

Risk: Authentication, connection, scope, or billing failures can interrupt connector use.

Mitigation: Follow the documented setup path only after a matching command failure, then resolve sign-in, Breezy HR connection, credential, scope, or billing issues before retrying.

## Reference(s):

- [Breezy HR homepage](https://breezy.hr/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Breezy HR connection](https://console.oomol.com/app-connections?provider=breezy_hr)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-breezy-hr)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON returned by the oo CLI; the skill itself provides action-selection and setup guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
