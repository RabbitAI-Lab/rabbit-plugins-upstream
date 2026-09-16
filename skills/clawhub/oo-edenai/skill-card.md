## Description:

Eden AI (edenai.co). Use this skill for ANY Eden AI request - reading, creating, and updating data. Whenever a task involves Eden AI, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Eden AI through an OOMOL-connected account, including listing available models and creating non-streaming chat completions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that may be executed without verification.

Mitigation: Review installation steps before use and prefer official package-manager or download-and-verify installation paths for the oo CLI.

Risk: The create_chat_completion action is tagged as a write action.

Mitigation: Confirm the exact payload and expected effect with the user before running the action.

## Reference(s):

- [Eden AI Homepage](https://www.edenai.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-edenai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions after inspecting live action schemas; write actions require payload confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
