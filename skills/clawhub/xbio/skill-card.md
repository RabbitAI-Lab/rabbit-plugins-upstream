## Description: <br>
X/Twitter CLI for reading, searching, and posting via cookies or Sweetistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[soanai](https://clawhub.ai/user/soanai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent operate the bird CLI for reading and searching X/Twitter content, checking authentication, and posting tweets or replies after explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The external bird CLI may use browser cookies or an API key with access to the user's X/Twitter account. <br>
Mitigation: Install only if the user trusts the bird CLI and Homebrew source, and consider a dedicated browser profile or API key to limit account exposure. <br>
Risk: The skill can post tweets or replies from the user's account. <br>
Mitigation: Require explicit user review and confirmation before running any tweet or reply command. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/soanai/skills/xbio) <br>
- [bird homepage](https://bird.fast) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the bird CLI; may use browser cookies or SWEETISTICS_API_KEY for authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
