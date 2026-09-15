## Description:

This skill handles GoSquared requests involving searching and reading data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve GoSquared Now overviews, visitor time series, token authorization details, and Trends aggregate metrics through an OOMOL-connected GoSquared account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may fetch and immediately execute remote installer scripts.

Mitigation: Install the oo CLI only through a verified, pinned, or package-manager flow that matches the user's trust requirements.

Risk: The skill can access GoSquared data through an OOMOL-connected account.

Mitigation: Run OOMOL login and GoSquared connection steps only when the user intentionally wants the skill to access that account's GoSquared data.

## Reference(s):

- [GoSquared homepage](https://www.gosquared.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gosquared)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented GoSquared connector guidance and command payloads; command responses are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
