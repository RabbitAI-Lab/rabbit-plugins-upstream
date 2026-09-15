## Description:

Benchmark Email lets an agent search and read Benchmark Email account, contact, and contact-list data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Benchmark Email account summaries, image storage plan details, contact details, contact-list summaries, and paginated contact-list search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that require review before execution.

Mitigation: Install the oo CLI through a verified package or downloaded artifact and check signatures or checksums before running installer scripts.

Risk: OOMOL-backed connector calls can read Benchmark Email account and contact-list data.

Mitigation: Use an OOMOL connection with appropriate Benchmark Email access and run only the read action needed for the user's task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-benchmark-email)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Benchmark Email Homepage](https://www.benchmarkemail.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
