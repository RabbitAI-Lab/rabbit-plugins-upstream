## Description:

Enables agents to operate Gemini through an OOMOL-connected account for content generation, embeddings, token counting, model listing, and video operation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to call Gemini via OOMOL for text, speech audio, image, and video generation, plus token counting, embeddings, model discovery, and video status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can run an unverified remote installer script if the oo CLI is missing.

Mitigation: Review the oo CLI installer source or use a verified manual install path before allowing installation.

Risk: Gemini write actions, such as video generation, can create new provider-side work or consume account resources.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running any action marked as write.

Risk: Authentication, provider connection, and billing setup expose account-level choices beyond normal Gemini actions.

Mitigation: Do not run login, connection, billing, or credential setup commands unless the user intentionally approves those setup steps.

## Reference(s):

- [Gemini API](https://ai.google.dev/gemini-api)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return generated content, embeddings, model metadata, operation status, or transit URLs depending on the selected Gemini action.]

## Skill Version(s):

1.0.4 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
