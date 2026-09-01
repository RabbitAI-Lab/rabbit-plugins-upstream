## Description:

Manages Typecho blog posts through the local typecho-cli tool, including creating, retrieving, updating, deleting, and listing categories for posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[coolingrabbit](https://clawhub.ai/user/coolingrabbit)

### License/Terms of Use:

MIT-0

## Use Case:

Blog owners and authorized agents use this skill to manage content in a configured Typecho blog. It supports publishing Markdown posts, retrieving and updating existing posts, selecting from existing categories, and deleting posts when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a blog API token that can read posts and modify content for the token's account.

Mitigation: Use a dedicated least-privilege token, keep ~/.config/typecho-cli/config.json private, and avoid passing the token on the command line.

Risk: Publish, update, or delete actions can change a live Typecho blog, and deletion is irreversible.

Mitigation: Review requested publish, update, and delete operations before execution, retrieve the full post before updates, and require confirmation before delete commands.

Risk: Category selection is limited to existing blog categories.

Mitigation: Run typecho-cli categories before publishing and ask the user to create a category manually when no existing category fits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/coolingrabbit/skills/typecho-publisher)
- [Publisher profile](https://clawhub.ai/user/coolingrabbit)
- [Typecho Publisher repository](https://github.com/CoolingRabbit/Typecho-Publisher)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and content-management guidance for an existing Typecho blog; CLI responses are JSON.]

## Skill Version(s):

4.1.0 (source: release evidence and SKILL.md frontmatter; plugin.json lists 4.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
