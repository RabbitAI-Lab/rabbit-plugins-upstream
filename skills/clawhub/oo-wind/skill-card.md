## Description:

Connects an agent to Wind financial data and research through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People with a connected Wind account use this skill to retrieve financial data, search news and disclosures, run Wind Alice analyses, and download reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes unverified remote installer commands that could execute arbitrary code.

Mitigation: Review the installer through OOMOL's official installation guide and prefer verified downloads or package-manager steps when available.

Risk: Write actions and Wind Alice research can change state or consume credits.

Mitigation: Confirm the exact write payload and potential Wind credit impact with the user before running these actions.

## Reference(s):

- [Wind homepage](https://market.windalice.com/)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Wind skill on ClawHub](https://clawhub.ai/oomol/skills/oo-wind)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands]

**Output Format:** [Text or Markdown responses based on JSON connector results, with report download links where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research tasks may require resuming an existing analysis.]

## Skill Version(s):

1.0.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
