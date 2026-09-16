## Description:

Hybrid Analysis enables agents to inspect Hybrid Analysis API authorization and retrieve file-hash search results, report overviews, report states, and report summaries through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to query Hybrid Analysis for file-hash investigations and sandbox report details from an agent workflow. It is intended for read-oriented malware-analysis lookup tasks after the user has connected Hybrid Analysis through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Use a verified, versioned official installation process for the oo CLI before relying on the skill.

Risk: The skill depends on OOMOL credentials and connector availability to reach Hybrid Analysis.

Mitigation: Install only when the user accepts OOMOL as a dependency and has connected Hybrid Analysis through the publisher's supported flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hybrid-analysis)
- [Hybrid Analysis Homepage](https://www.hybrid-analysis.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Hybrid Analysis Skill Icon](https://static.oomol.com/logo/third-party/hybrid_analysis.svg)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live action schemas before running read-oriented connector actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
