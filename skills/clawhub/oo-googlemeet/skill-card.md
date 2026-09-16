## Description:

Google Meet (workspace.google.com). Use this skill for ANY Google Meet request: reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workspace operators use this skill to manage Google Meet spaces and inspect conference records, participants, recordings, transcripts, transcript entries, and smart notes through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could be unsafe if run without review.

Mitigation: Review setup steps manually and do not run remote installer commands blindly.

Risk: The skill can end an active Google Meet conference, and the security summary notes this action is under-labeled.

Mitigation: Require explicit user confirmation of the target meeting before ending any active conference.

Risk: State-changing Google Meet actions can create or update meeting spaces.

Mitigation: Confirm the exact payload and expected effect before running write actions.

## Reference(s):

- [Google Meet product page](https://workspace.google.com/products/meet/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-googlemeet)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Google Meet join URLs, resource identifiers, record summaries, transcript references, and setup recovery instructions depending on the requested action.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
