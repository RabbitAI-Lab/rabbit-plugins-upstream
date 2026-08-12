## Description:

Generates client-ready, single-page HTML proposals for freelancers, solo consultants, and small studios from a brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoquanlong](https://clawhub.ai/user/guoquanlong)

### License/Terms of Use:

MIT-0

## Use Case:

Freelancers, solo consultants, and small studios use this skill to turn a short client brief into a polished sales proposal, quote, or pitch document that can be previewed, printed to PDF, or sent to a client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated client-facing proposals may include the default non-user WeChat or email contact information.

Mitigation: Replace CONTACT_LINE, WECHAT, and WEBSITE with the user's own details before generating client-ready output.

Risk: The contact watermark is enabled by default and may add a visible lead-generation pill to shared HTML proposals.

Mitigation: Set SHOW_CONTACT_WATERMARK to false when the user does not want a contact watermark in the generated proposal.

Risk: Proposal copy, pricing, and claims may be inaccurate or unsuitable for a specific client engagement.

Mitigation: Review the generated proposal before sending and confirm pricing, scope, claims, and contact details.

## Reference(s):

- [Proposal Structure Reference](artifact/references/proposal-structure.md)
- [ClawHub Skill Page](https://clawhub.ai/guoquanlong/skills/freelance-proposal-gen)
- [ClawHub Publisher Profile](https://clawhub.ai/user/guoquanlong)

## Skill Output:

**Output Type(s):** [text, code, configuration, shell commands]

**Output Format:** [A fields JSON plan plus a generated self-contained HTML proposal file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs offline without external API keys; generated proposals should be reviewed before client use, and the contact watermark can be disabled.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
