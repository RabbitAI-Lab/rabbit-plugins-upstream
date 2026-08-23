## Description:

Converts user-provided article links from WeChat, Zhihu, or general webpages into AI-analyzed spoken podcast audio through the TingDong backend and Edge-TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn article URLs into short, conversational, or deep-dive podcast audio for listening workflows. It is intended to run only when the user explicitly asks for an audio, voice, or podcast version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article URLs, article text, user identifiers, and bearer-token-authenticated requests may be sent to the TingDong backend over plain HTTP.

Mitigation: Prefer a trusted HTTPS self-hosted backend, avoid private or sensitive content, and protect the API token as a credential.

Risk: The skill includes scraping guidance for sites with access controls, anti-scraping measures, or terms that may restrict automated access.

Mitigation: Use it only for content the user is authorized to process, respect site terms and access restrictions, and ask the user to paste content when automated retrieval is not appropriate.

## Reference(s):

- [TingDong ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/tingdong)
- [API documentation](artifact/references/api_docs.md)
- [Content source strategy](artifact/references/content_sources.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task identifiers, status text, and generated audio URLs from the TingDong backend.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
