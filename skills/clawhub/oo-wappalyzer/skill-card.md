## Description:

Enables agents to use Wappalyzer through an OOMOL-connected account for website technology lookups, subdomain discovery, credit balance checks, and email verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to inspect website technology stacks, discover website-serving subdomains, verify emails, and check Wappalyzer API credits through an OOMOL-connected Wappalyzer account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote shell and PowerShell installer commands that may be difficult to verify before execution.

Mitigation: Install the oo CLI from a trusted, versioned, verifiable source and review setup commands before running them.

## Reference(s):

- [Wappalyzer homepage](https://www.wappalyzer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wappalyzer)

## Skill Output:

**Output Type(s):** [Shell commands, JSON payloads, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Wappalyzer connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
