## Description:

A secure data analysis workflow suite based on MGC Blackbox that provides credential protection, zero-exposure script application, script sealing collaboration, knowledge management, and a Data Analyst Agent system prompt template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Data analysts, teams, and agent builders use this skill to manage local MGC Blackbox workflows for credentials, user-owned scripts, script sealing, and reusable analysis knowledge with explicit authorization before sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags inconsistent promises around credential, script, and knowledge access.

Mitigation: Review the suite before installation and confirm MGC Blackbox data flow, authorization prompts, and local storage behavior in the target environment.

Risk: Stored credentials, scripts, and knowledge may contain sensitive business material.

Mitigation: Use only trusted user-owned scripts, avoid highly sensitive secrets unless the actual MGC data flow is understood, and keep organizational security and compliance review in the workflow.

Risk: Authorized knowledge retrieval may be visible to the AI session.

Mitigation: Treat retrieved knowledge as potentially exposed to the session unless independently proven otherwise, and avoid retrieving confidential knowledge into untrusted sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/data-analyst-secure-suite)
- [MGC Blackbox project homepage](https://github.com/zkeviny/MGC-Blackbox)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks, command examples, and agent prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sensitive actions are framed around explicit user authorization and local MGC Blackbox workflows.]

## Skill Version(s):

1.1.2 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
