## Description:

Use Diffbot through an OOMOL-connected account to extract public article URLs and return normalized article data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to run Diffbot actions through the oo CLI with an OOMOL-connected Diffbot account, especially extracting structured article data from public URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that could be executed without review.

Mitigation: Install oo from trusted, versioned release artifacts or official package instructions, and review installer contents before execution.

Risk: Diffbot access is mediated through OOMOL, which handles connector credentials server-side.

Mitigation: Use Diffbot credentials and scopes appropriate for the intended data access, and install the skill only when OOMOL is an acceptable intermediary.

## Reference(s):

- [Diffbot Homepage](https://www.diffbot.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-diffbot)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are returned as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
