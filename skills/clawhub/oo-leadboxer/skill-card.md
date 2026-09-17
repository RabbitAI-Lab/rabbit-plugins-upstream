## Description:

LeadBoxer helps agents search and read enrichment data for domains and IP addresses through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run LeadBoxer domain and IP enrichment through the OOMOL oo CLI. It supports inspecting live action schemas before submitting JSON payloads for lookup requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to run remote installer scripts directly in a shell, which can execute unverified code.

Mitigation: Run those installer commands only after trusting OOMOL's installer channel; prefer a verified, signed, or package-manager-based install path when available.

## Reference(s):

- [LeadBoxer homepage](https://www.leadboxer.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [LeadBoxer connection page](https://console.oomol.com/app-connections?provider=leadboxer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector run responses are requested as JSON and include data plus execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
