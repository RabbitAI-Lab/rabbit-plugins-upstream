## Description:

Conclave is a multi-agent reasoning skill that orchestrates multiple AI CLIs into structured debates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mclyang](https://clawhub.ai/user/mclyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and decision makers use Conclave to convene multiple AI agents for structured debate, rebuttal, convergence, and final adjudicated Markdown reports on high-stakes decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debate briefs, agent outputs, final reports, and logs are archived persistently under the user's home directory.

Mitigation: Use the skill only with data approved for local retention, and add review, redaction, cleanup, or retention controls for archived debates.

Risk: Prompts and debate content are sent to configured external AI CLIs and providers.

Mitigation: Use only data approved for those providers, verify provider configuration before preflight, and document any provider restrictions in the brief.

Risk: Credential troubleshooting references keychain passwords, API keys, and local auth files.

Mitigation: Use secure interactive authentication workflows and avoid placing passwords, API keys, or credentials in prompts, briefs, logs, or archived files.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/MCLYang/conclave-skill)
- [ClawHub skill page](https://clawhub.ai/mclyang/skills/conclave-skill)
- [Panelist roster and CLI parameters](artifact/references/panelists.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, process notes, file paths, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a persistent debate archive with final.md, minutes.md, index.md, round notes, and preflight logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; source skill frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
