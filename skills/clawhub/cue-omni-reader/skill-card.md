## Description:

Omni Reader parses URLs and files, including PDFs, Office documents, images, scans, audio, video, web pages, and archives, into Markdown or clean text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to convert local files or URLs into Markdown or text for OCR extraction, transcription, summarization, and downstream document processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install and run a local MCP bridge with API-key, local-file, network, cache, and agent-configuration authority.

Mitigation: Install only if you trust Cue and the npm bridge, prefer URL-only configuration when local files are not needed, and review MCP configuration changes before setup.

Risk: Broad local-file roots or casual credential handling can expose sensitive files or API keys.

Mitigation: Keep OMNI_ALLOWED_ROOTS narrow, store the API key in a secret store, and submit sensitive or restricted-login content only when authorized.

Risk: Using @latest for the npm bridge can change deployed code without a repeatable review point.

Mitigation: Pin @cueai/omni-reader-mcp to a reviewed version for reproducible deployment.

Risk: Unused local configuration, caches, or result artifacts may retain access paths or parsed content.

Mitigation: Run the documented clean and uninstall steps when the bridge is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Omni Reader product page](https://cuecue.cn/hub/omni-reader)
- [CLI manual](artifact/cli-manual.md)
- [Cue API key documentation](https://cuecue.cn/hub/api-key)
- [MCP catalog endpoint](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or clean text, with JSON MCP responses and shell/configuration snippets when setup or troubleshooting is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Parses one source per request; local bridge mode can page, export, and discard large results, while the remote endpoint returns completed results inline.]

## Skill Version(s):

1.2.13 (source: server release metadata; artifact frontmatter reports 1.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
