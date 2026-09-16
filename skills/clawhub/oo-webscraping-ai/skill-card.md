## Description:

WebScraping.AI helps agents extract visible text, rendered HTML, selected HTML, and account details through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call WebScraping.AI through an OOMOL-connected account for page text extraction, rendered HTML retrieval, selected HTML extraction, and account quota checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts without verification.

Mitigation: Review the installer source before running it, or install the oo CLI through a verified, pinned, or package-manager-based method.

Risk: Connector calls are brokered through an OOMOL-connected WebScraping.AI account.

Mitigation: Connect the account only when this brokerage is intended, and review requested connector schemas and payloads before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-webscraping-ai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [WebScraping.AI Homepage](https://webscraping.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include scraped text, rendered HTML, selected HTML, account quota data, and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
