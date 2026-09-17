## Description:

Benchmark Email helps agents retrieve Benchmark Email account and contact-list data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Benchmark Email account details and read contacts or contact-list summaries from an OOMOL-connected Benchmark Email account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can lead users to run an unverified remote installer script.

Mitigation: Prefer installing the oo CLI from a trusted, versioned source with checksum or signature verification.

Risk: Connecting Benchmark Email allows OOMOL to broker connector access to account data.

Mitigation: Connect Benchmark Email only after confirming that this access model is acceptable for the account and data involved.

## Reference(s):

- [Benchmark Email homepage](https://www.benchmarkemail.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-benchmark-email)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Benchmark Email requests.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
