## Description:

Omni Reader helps an agent parse local files or web URLs into Markdown or clean text, covering PDFs, Office documents, images, scans, audio, video, web pages, and archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users can use this skill when they need OCR, document parsing, audio or video transcription, table extraction, or webpage conversion into Markdown for downstream analysis. The skill is especially relevant when the source is a user-approved local path or an HTTP(S) URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents, URLs, and parsed content may be processed by Cue-operated services, and the security review notes conflicting privacy/data-flow statements.

Mitigation: Use the skill only for data you are comfortable sending to Cue services, avoid confidential sources, and review the data-flow behavior before deployment.

Risk: The external npm Bridge can access the configured API key and user-approved local file roots.

Mitigation: Use a revocable API key, keep OMNI_ALLOWED_ROOTS limited to the minimum required directories, and review the bridge package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)
- [Cue API key documentation](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return inline results or artifact handles for large asynchronous parses; local Bridge results may be read in chunks, outlined, saved, or discarded.]

## Skill Version(s):

1.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
