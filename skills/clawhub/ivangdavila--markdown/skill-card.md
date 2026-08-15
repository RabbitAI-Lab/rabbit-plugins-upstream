## Description: <br>
Helps agents write, fix, convert, lint, and safely render Markdown across GitHub, MDX, Pandoc, documentation sites, and chat platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and support teams use this skill to produce portable Markdown, debug renderer-specific failures, convert documents, configure Markdown tooling, and assess untrusted Markdown before rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local Markdown notes may capture document preferences, project pointers, renderer quirks, or other durable context. <br>
Mitigation: Install only if this local note behavior is acceptable, review the configured Clawic data files periodically, and avoid persisting sensitive document content. <br>
Risk: Documentation examples can contain tokens, connection strings, CI secrets, or other credentials. <br>
Mitigation: Strip live secret values before saving or reusing documents, replacing them with clear pointers such as environment-variable or vault references. <br>
Risk: Untrusted Markdown, HTML, or MDX can create rendering and execution risks if handled as trusted content. <br>
Mitigation: Sanitize rendered HTML, apply URL-scheme allowlists, and do not render untrusted MDX as executable content. <br>


## Reference(s): <br>
- [ClawHub Markdown Skill](https://clawhub.ai/ivangdavila/skills/markdown) <br>
- [Clawic Markdown Skill](https://clawic.com/skills/markdown) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with code blocks, diffs, configuration snippets, command examples, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local Markdown preferences and project notes under configured Clawic data paths when the host agent permits file access.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
