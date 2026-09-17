## Description:

ipdata.co (ipdata.co). Use this skill for ANY ipdata.co request - searching and reading data. Whenever a task involves ipdata.co, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query ipdata.co through an OOMOL-connected account for IP geolocation, ASN, carrier, company, currency, language, time zone, flag, EU, caller-IP, threat intelligence, and bulk lookup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not allow an agent to run curl|bash or irm|iex installer commands automatically; use a verified package or inspect and verify the installer before installation.

Risk: IP addresses submitted for lookup are sent through OOMOL's connector to ipdata.co under the connected account.

Mitigation: Only query IP addresses the user is allowed to share with OOMOL and ipdata.co, and review sensitive or bulk lookup payloads before execution.

## Reference(s):

- [ipdata.co homepage](https://ipdata.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ipdata-co)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload or response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before constructing payloads; connector run responses are JSON objects.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
