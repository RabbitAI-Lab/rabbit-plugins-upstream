## Description:

Reimagines a supplied song recording as a new cover with a fresh genre, arrangement, or vocal direction, then guides review of the generated performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and music enthusiasts use the skill to turn a supplied song recording into a genre-shifted cover and review the generated arrangement, vocals, lyrics, and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants shared access to other media capabilities, including paid generation and voice management; a selected recording is uploaded and installation/system analytics are reported.

Mitigation: Approve only if you accept the shared access and paid-generation scope; review the recording before upload and revoke access in the Beatra Console when no longer needed.

Risk: Removing this package may leave a shared Beatra connection active for other installed skills.

Mitigation: After uninstalling, check the Beatra Console and explicitly revoke the shared connection if you no longer need it.

## Reference(s):

- [AI Song Cover Studio](https://beatra.ai/skills/ai-song-cover-studio)
- [Beatra MCP service](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Audio, Text, Guidance]

**Output Format:** [Generated audio artifact or link with a concise performance review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One cover per run, based on a user-supplied reference recording.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
