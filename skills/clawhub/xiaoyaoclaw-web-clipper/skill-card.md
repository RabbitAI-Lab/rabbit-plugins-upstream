## Description:

OpenClaw Web Clipper saves user-specified web pages as clean local Markdown with YAML frontmatter, dual-engine extraction, Chinese-safe filenames, batch clipping, deduplication, and output ready for knowledge-base indexing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and knowledge-base maintainers use this skill to clip specified public web pages into local Markdown files for later search, citation, or knowledge-base indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clipping a page contacts the target website and exposes ordinary request metadata such as IP address and user agent.

Mitigation: Clip only user-approved URLs; the artifact limits fetching to public http/https targets on ports 80 and 443, uses GET requests, omits cookies and authorization headers, and bounds response size.

Risk: The skill creates persistent Markdown files and a deduplication index in the user's home directory.

Mitigation: Review or set CLIPPER_OUTPUT_DIR or --dir before use; the artifact validates output paths and rejects destinations outside the home directory or sensitive home subdirectories.

Risk: Fetched web page content may contain prompt-injection text or misleading instructions.

Mitigation: Treat clipped content as untrusted reference data; the artifact adds an untrusted-content banner and sanitizes metadata fields before writing Markdown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-web-clipper)
- [Project documentation](https://github.com/dtsola/xiaoyaoclaw-web-clipper)
- [OpenClaw overview](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)

## Skill Output:

**Output Type(s):** [markdown, text, shell commands, configuration, guidance]

**Output Format:** [Markdown files with YAML frontmatter plus terminal status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a local deduplication index in the selected output directory; batch mode reports successful, skipped, and failed clips.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
