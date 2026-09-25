## Description:

Generate professional HTML and PDF presentations from markdown content, URLs, or topics with AI-generated illustrations, keyboard navigation, and automatic PDF export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nhype](https://clawhub.ai/user/nhype)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, designers, and content creators use this skill to turn a topic, URL, markdown file, or provided text into a styled presentation with editable content, an interactive HTML deck, slide screenshots, AI-generated visuals, and a PDF export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled image tool can read and upload local image files supplied to the edit workflow.

Mitigation: Run the skill in an isolated project or container and keep sensitive local files outside paths available to the agent and MCP server.

Risk: The bundled image tool can write generated image outputs to arbitrary writable absolute paths.

Mitigation: Restrict image output paths to a dedicated presentation/images directory and review requested file paths before execution.

Risk: Slide text, prompts, fetched URL content, and edited source images may be sent to OpenAI or Azure OpenAI.

Mitigation: Use a least-privileged API key and avoid submitting confidential or regulated material unless the configured provider and account are approved for that data.

Risk: The release security verdict is suspicious and requires review before installation.

Mitigation: Review the source, scan results, dependency pins, and MCP server exposure before using the skill in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nhype/skills/generate-presentation)
- [Presentation Generation Skill README](artifact/README.md)
- [OpenAI GPT Image MCP Server README](artifact/mcp-servers/openai-gpt-image/README.md)
- [Example presentation content](artifact/examples/example-content.md)
- [Agent Skills](https://agentskills.io)
- [OpenAI API keys](https://platform.openai.com/api-keys)
- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [Pillow documentation](https://pillow.readthedocs.io/)
- [Claude Code skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with generated HTML, PDF, PNG images, and editable markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces presentation/slides.html, presentation/presentation.pdf, presentation/slide_N.png, presentation/images/, and presentation/content.md when prerequisites are available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
