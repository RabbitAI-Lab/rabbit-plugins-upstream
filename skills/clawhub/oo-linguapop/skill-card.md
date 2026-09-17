## Description:

Linguapop skill routes reading, creating, and updating Linguapop data through the OOMOL oo CLI connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Linguapop connector schemas, list available placement-test languages, and create placement-test invitations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified remote installer scripts that could execute arbitrary code.

Mitigation: Review the oo CLI installer through an official source, prefer a pinned or package-manager installation with integrity verification, and avoid running installer commands automatically.

Risk: The send_invitation action changes Linguapop state and may email a candidate or create a kiosk code.

Mitigation: Confirm the exact recipient, payload, callback or return URL, and intended effect with the user before sending an invitation.

## Reference(s):

- [ClawHub Linguapop Skill](https://clawhub.ai/oomol/skills/oo-linguapop)
- [Linguapop Homepage](https://www.linguapop.eu/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Linguapop Icon](https://static.oomol.com/logo/third-party/Linguapop.svg)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector schema and run commands; write actions require user confirmation of recipient and payload before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
