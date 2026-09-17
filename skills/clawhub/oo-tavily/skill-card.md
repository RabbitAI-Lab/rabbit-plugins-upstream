## Description:

Tavily lets agents use OOMOL-connected Tavily actions for web search, crawling, URL mapping, content extraction, asynchronous research tasks, and account usage checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to operate Tavily through an OOMOL-connected account, including search, crawl, map, extract, research, and usage-check workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to execute a remote installer directly in a shell without verification.

Mitigation: Review the installer path before use, prefer a trusted versioned release or package manager with checksum or signature verification, and avoid running curl-to-bash or irm-to-iex commands automatically.

Risk: Write actions can change Tavily state when an agent constructs and submits a payload.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval for any destructive action.

## Reference(s):

- [Tavily homepage](https://tavily.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Tavily skill page](https://clawhub.ai/oomol/skills/oo-tavily)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Tavily action names, schema-inspection commands, and confirmation guidance for actions that change state.]

## Skill Version(s):

1.0.4 (source: server evidence, release metadata, and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
