## Description: <br>
Operate Bluesky through an OOMOL-connected account for profile lookup, post search, and confirmed text post creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to handle Bluesky tasks through the oo CLI, including reading profiles, searching posts, and creating text posts in an authenticated OOMOL-connected account after explicit confirmation for writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create Bluesky posts in the connected account. <br>
Mitigation: Confirm the exact payload and account effect with the user before running actions tagged as write. <br>
Risk: Setup commands can install the oo CLI or start an OOMOL login flow. <br>
Mitigation: Run installer, login, or connection steps only when a command fails because required setup is missing. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Bluesky homepage](https://bsky.social) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
