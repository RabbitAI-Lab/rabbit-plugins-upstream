## Description:

Exports the current logged-in Xiaohongshu user's favorites into local Markdown note files with source links, text, media URLs, resumable offset/count batching, and a summary JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to back up, search, and reuse their own Xiaohongshu favorite notes as local Markdown files for personal knowledge management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The exporter uses the user's logged-in Chrome/Xiaohongshu session and saves private favorite contents to local files.

Mitigation: Run it only in a trusted local environment, choose an output directory with appropriate access controls, and review generated files before sharing them.

Risk: Exported Markdown may contain signed image or video URLs that expose private or time-limited media access.

Mitigation: Treat exported Markdown as sensitive and avoid publishing or syncing it to untrusted services.

Risk: Security evidence reports an undocumented obfuscated wc3-code.mjs helper that can send prompt or file content to a local or overridden LLM endpoint if invoked.

Mitigation: Audit or remove the helper before installation, do not invoke it with sensitive files, and install only if the publisher is trusted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/fatmind/skills/xhs-fav-export)
- [webclaw3 browser automation dependency](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [Xiaohongshu website](https://www.xiaohongshu.com/)

## Skill Output:

**Output Type(s):** [markdown, json, files]

**Output Format:** [Local Markdown files plus JSON summary/status metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a logged-in Chrome/Xiaohongshu session and webclaw3 browser relay; media is stored as URLs rather than downloaded files.]

## Skill Version(s):

1.0.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
