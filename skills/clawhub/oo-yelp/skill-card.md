## Description:

Yelp connector for searching businesses, finding businesses by phone number, and retrieving business details through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Yelp businesses by keyword, location, or phone number and retrieve business details without handling raw Yelp credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer command pipelines for the oo CLI.

Mitigation: Review installer commands before use and prefer a verified release or package-manager installation path with checksums or signatures.

Risk: The security verdict flags the release as suspicious because of unverified remote installer scripts, even though the Yelp actions are mostly coherent and read-only.

Mitigation: Treat first-time setup as an elevated-trust step and run Yelp connector actions only after the CLI installation source is validated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-yelp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Yelp homepage](https://www.yelp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples; connector action responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Yelp lookup actions; OOMOL handles Yelp credentials server-side.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
