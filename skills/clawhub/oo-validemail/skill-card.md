## Description:

Helps agents check ValidEmail verification credits and verify individual email addresses through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents with a connected ValidEmail account can check their remaining verification credits and verify one email address at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions suggest running an unverified installer script downloaded from the internet.

Mitigation: Review the installation path and use verified official instructions or validate the installer's checksum or signature before running it.

Risk: Connecting an account or verifying emails may use OOMOL services and spend ValidEmail verification credits.

Mitigation: Connect an account and run email verification only when intended; check the available balance before credit-consuming requests.

## Reference(s):

- [ValidEmail](https://www.validemail.net/)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ValidEmail skill listing](https://clawhub.ai/oomol/skills/oo-validemail)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON action results and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Balance checks do not use credits; each email verification uses one credit, and unknown results are inconclusive.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
