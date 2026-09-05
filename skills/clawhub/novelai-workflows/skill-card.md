## Description:

NovelAI creative workflows for OpenClaw: fiction context, chapter planning, image prompting, V5/V4.5 generation, img2img, inpainting, Vibe/Director tools, cost-aware execution, and secret-safe asset records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[techotaku39](https://clawhub.ai/user/techotaku39)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to coordinate NovelAI-assisted fiction workflows and image generation, including chapter planning, bounded story context, prompt preparation, cost checks, image edits, and safe asset metadata records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NovelAI image and editing operations can consume account resources.

Mitigation: Show the planned model, size, steps, sample count, and estimated Anlas before ambiguous batches, high-resolution work, or repeated retries.

Risk: The configured NovelAI provider or MCP server receives prompts and uses the operator's NovelAI token.

Mitigation: Keep the token in the host environment or SecretRef, review the pinned third-party MCP server separately, and avoid highly sensitive prompt content.

Risk: Prompts and generation details may be saved in local project metadata.

Mitigation: Record reproducibility metadata without credentials and avoid storing secrets or private account details in generation records.

Risk: Some advertised capabilities may be unavailable on the active host, including dedicated upscaling in the reference test.

Mitigation: Inspect the active MCP catalog and tool schemas before use, and report missing or failed operations without silently substituting another provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/techotaku39/skills/novelai-workflows)
- [OpenClaw Skills documentation](https://docs.openclaw.ai/skills)
- [OpenClaw ClawHub quickstart](https://docs.openclaw.ai/clawhub/quickstart)
- [NovelAI Image MCP](https://github.com/xinvxueyuan/NovelAI-Image-MCP)
- [NovelAI image models](https://docs.novelai.net/en/image/models/)
- [NovelAI text models](https://docs.novelai.net/en/text/models/)
- [NovelAI persistent API token](https://docs.novelai.net/en/text/usersettings/account/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and structured generation metadata guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute NovelAI text and image workflows through configured providers and MCP tools; generation steps can consume account resources after user approval.]

## Skill Version(s):

0.1.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
