## Description:

Connects to 得到大脑 through the official getnote CLI to authorize access, diagnose or upgrade the CLI, and save, search, read, and manage notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT-0

## Use Case:

People using 得到大脑 can use this skill to connect an AI assistant through the official getnote CLI to save, find, read, and organize notes and knowledge-base content, manage tags, and diagnose the connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connection workflow synchronizes five other AI skills without separate approval.

Mitigation: Before connecting, require separate approval for synchronizing other skills and provide a clear list of affected files and overwrite behavior.

Risk: Browser authorization grants account access, and the external CLI's actual behavior is unverified.

Mitigation: Keep authorization in the user's browser and verify command outcomes from the CLI's structured results.

## Reference(s):

- [GetNote skill release on ClawHub](https://clawhub.ai/iswalle/skills/getnote)
- [Publisher profile](https://clawhub.ai/user/iswalle)
- [Official GetNote CLI package](https://www.npmjs.com/package/@getnote/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Text summaries]

**Output Format:** [CLI operations with JSON results and concise user-facing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or modify the currently authorized 得到大脑 account according to the user's request.]

## Skill Version(s):

2.4.1 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
