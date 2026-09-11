## Description:

here.now lets agents publish websites and files to live URLs in seconds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use here.now to publish local files, folders, generated websites, and workspace sites to live URLs, manage access controls, and use private Drive storage for persistent agent files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists account credentials and local publish state that may expose tokens if mishandled.

Mitigation: Use only with files intended for upload, prefer a pinned or local install, treat ~/.herenow/credentials and .herenow/state.json as sensitive, and remove or revoke keys and tokens when no longer needed.

Risk: Drive exports may write files outside an intended export folder until path containment is fixed.

Mitigation: Avoid exporting Drive contents from untrusted shares and review exported paths before using the files.

## Reference(s):

- [here.now documentation](https://here.now/docs)
- [here.now OpenAPI specification](https://here.now/openapi.json)
- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, URLs, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live site URLs, access-control guidance, Drive sharing guidance, and credential handling notes.]

## Skill Version(s):

1.28.0 (source: server release evidence and artifact SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
