## Description:

Figma integration for browsing team projects and files, reading design structure, exporting images, managing comments, viewing version history, inspecting components and styles, and retrieving design variables through MorphixAI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paul-leo](https://clawhub.ai/user/paul-leo)

### License/Terms of Use:


## Use Case:

Developers, designers, and design-system maintainers use this skill to inspect Figma workspaces, retrieve file and node details, export assets, review comments and versions, and examine components, styles, and design tokens from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Figma data through a linked MorphixAI account.

Mitigation: Install only for users who are comfortable granting the permissions available to the linked Figma account.

Risk: The MORPHIXAI_API_KEY credential could expose access if committed to source control or logged.

Mitigation: Keep MORPHIXAI_API_KEY out of source control and logs.

Risk: Comment posting or deletion can affect shared or business Figma workspaces.

Mitigation: Require clear confirmation before posting or deleting Figma comments.

## Reference(s):

- [ClawHub Figma skill page](https://clawhub.ai/paul-leo/skills/figma-2)
- [MorphixAI API keys](https://morphix.app/api-keys)
- [MorphixAI connections](https://morphix.app/connections)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown guidance with inline tool-call examples and configuration commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MORPHIXAI_API_KEY and a linked Figma account through MorphixAI.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
