## Description:

Use Clip2MD to connect an AI assistant, save web pages as Markdown, check quota, query task status, wait for completion, and retrieve results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clip2md](https://clawhub.ai/user/clip2md)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and assistant operators use this skill to connect an AI assistant to Clip2MD, submit individual HTTP(S) URLs for web clipping, monitor task status and quota, and retrieve generated Markdown when tasks complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a credentialed CLI that can access a Clip2MD account from the local assistant environment.

Mitigation: Install only when the publisher and runtime environment are trusted, use the standard connect flow, and run disconnect when assistant access is no longer needed.

Risk: Changing CLIP2MD_API_BASE can direct credentialed requests away from the default production API.

Mitigation: Set CLIP2MD_API_BASE only in controlled testing or private deployments.

Risk: The legacy token command can store a real token in local configuration.

Mitigation: Avoid the legacy token command with real credentials and prefer the standard connection flow.

## Reference(s):

- [Clip2MD Skill Page](https://clawhub.ai/clip2md/skills/clip2md)
- [Clip2MD Web App](https://clip2.md)
- [Clip2MD API Endpoint](https://api.clip2md.cn/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, task status, quota details, connection status, and Markdown clipping results.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
