## Description:

Facilitates structured exploration and clarification of user intent to create clear, approved designs before any implementation begins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn creative work, new features, components, and behavior changes into approved designs before implementation. It guides the agent through project-context review, clarifying questions, approach comparison, spec writing, self-review, and handoff to implementation planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad mandatory triggers and can slow or block implementation until a design is approved.

Mitigation: Install it only when a strict design-first workflow is desired, and confirm scope before allowing it to govern routine work.

Risk: The workflow can persist design documents and commit them to git.

Mitigation: Require explicit confirmation before file writes or git commits, especially in shared or production repositories.

Risk: The optional visual companion runs a local browser server and stores click selections and mockup files.

Mitigation: Use the companion only after user approval, keep the session URL private, stop the server when finished, and exclude persisted companion files from version control when appropriate.

## Reference(s):

- [Brainstorming skill page](https://clawhub.ai/pmuhammadagus-byte/skills/brainstorming)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, design-spec prose, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local design documents and browser companion HTML when the user approves that workflow.]

## Skill Version(s):

1.0.0 (source: server evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
