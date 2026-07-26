## Description: <br>
Otter.ai (otter.ai). Use this skill for ANY Otter.ai request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to let an agent search, list, and read Otter.ai workspace, channel, conversation, and conversation-audio information through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Otter.ai prompts may cause the agent to access private meeting or transcript information sooner than the user intended. <br>
Mitigation: Review prompts involving private meetings, transcript links, or workspace data before allowing the agent to retrieve or summarize Otter.ai content. <br>
Risk: Conversation audio actions can return temporary download URLs for meeting audio. <br>
Mitigation: Request audio URLs only when the task requires audio access, and avoid exposing or persisting the URL beyond the current user-approved workflow. <br>
Risk: Authentication, connection, and billing setup commands can change account state or require user action. <br>
Mitigation: Use setup steps only after a matching CLI, authentication, connection, or billing failure, and keep normal operation limited to the already connected OOMOL account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-otter-ai) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Otter.ai Homepage](https://otter.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running Otter.ai read actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
