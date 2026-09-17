## Description:

Nasdaq Data Link (data.nasdaq.com) skill for searching and reading Nasdaq Data Link data through the OOMOL Nasdaq connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and retrieve Nasdaq Data Link data through an OOMOL-connected account, including datatable metadata, bulk exports, row queries, dividends, analyst ratings, and end-of-day quote data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts that are executed directly in a shell.

Mitigation: Install the oo CLI from a verified, versioned package when possible, or inspect and verify the installer before running it.

Risk: Nasdaq query data is sent through OOMOL's connector service during normal use.

Mitigation: Send only the data needed for the Nasdaq Data Link request and avoid including unrelated local or sensitive information.

## Reference(s):

- [Nasdaq Data Link homepage](https://data.nasdaq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nasdaq)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal action responses are JSON objects containing data and meta.executionId when returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
