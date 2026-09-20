## Description:

Headless browser automation CLI optimized for AI agents with accessibility tree snapshots and ref-based element selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unfall103-debug](https://clawhub.ai/user/unfall103-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to automate browser workflows through the agent-browser CLI, including navigation, ref-based interaction, session isolation, state persistence, extraction, and network control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global npm installation or system dependency installation can introduce supply-chain or elevated-privilege exposure.

Mitigation: Install from a trusted npm source, prefer a pinned local dependency, and avoid elevated system dependency installation unless necessary.

Risk: Saved browser state, cookies, and storage values can contain credentials or session tokens.

Mitigation: Create saved auth state only for authorized accounts, keep files private, avoid logging their contents, and delete them when no longer needed.

Risk: Browser automation can perform real actions on websites when given active sessions.

Mitigation: Review target URLs and proposed actions before execution, use isolated sessions, and reserve headed mode or screenshots for visual verification when needed.

## Reference(s):

- [agent-browser homepage](https://github.com/vercel-labs/agent-browser)
- [ClawHub skill page](https://clawhub.ai/unfall103-debug/skills/agent-browser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on ref-based browser element identifiers, JSON snapshots, CLI sessions, saved browser state, and installation commands.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
