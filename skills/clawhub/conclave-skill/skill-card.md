## Description:

Conclave is a multi-agent reasoning skill that orchestrates multiple AI CLIs into structured debates. Each agent independently analyzes the problem, challenges competing arguments, identifies flaws and contradictions, and refines the reasoning through multiple rounds of discussion - helping you reach more reliable conclusions than relying on a single AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mclyang](https://clawhub.ai/user/mclyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and decision-makers use Conclave to structure high-stakes decisions as multi-agent debates that produce a chair-adjudicated final report and process minutes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global package changes and CLI self-updates may alter the user's environment.

Mitigation: Run install checks with --check-only where possible, use --skip-update during preflight when updates are not desired, and evaluate the skill in an isolated environment before regular use.

Risk: Debate topics and final drafts may be sent to multiple third-party AI providers.

Mitigation: Avoid regulated, classified, proprietary, or sensitive personal data unless the user has reviewed the relevant provider policies and accepted the sharing.

Risk: Full debate records and calibration logs persist locally and may be exported into the working directory.

Mitigation: Run Conclave from an isolated project directory and periodically remove old records with the bundled cleanup script or manual deletion of ~/.hermes/debates.

Risk: Credential and auth-state probing can reveal which providers are configured even when secret values are not read.

Mitigation: Use a least-privilege user account or sandboxed workstation, and review preflight output before sharing logs.

## Reference(s):

- [Conclave skill page](https://clawhub.ai/mclyang/skills/conclave-skill)
- [MCLYang publisher profile](https://clawhub.ai/user/mclyang)
- [Panelist roster](references/panelists.md)
- [Consensus protocol v1.1](references/consensus-protocol-v1.md)
- [Manus tasks API](https://api.manus.im/v1/tasks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, process minutes, debate files, and shell/configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent per-debate files, including briefs, panelist outputs, verdicts, final reports, and meeting minutes.]

## Skill Version(s):

1.6.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
