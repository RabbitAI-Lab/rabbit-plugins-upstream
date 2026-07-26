## Description: <br>
Alexandrie lets an agent create, read, update, delete, and search Markdown notes in an Alexandrie note-taking account through a shell client and REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eth3rnit3](https://clawhub.ai/user/eth3rnit3) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and individual operators use this skill to manage notes in a configured Alexandrie account from an agent session, including listing, reading, searching, creating, updating, and deleting Markdown notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, create, update, and delete private notes in a live Alexandrie account. <br>
Mitigation: Install only for an account you control, require explicit confirmation before update or delete operations, protect the environment file that stores the password, and log out or remove temporary cookie files when finished. <br>


## Reference(s): <br>
- [Alexandrie Skill on ClawHub](https://clawhub.ai/eth3rnit3/skills/alexandrie) <br>
- [Alexandrie app](https://notes.eth3rnit3.org) <br>
- [Alexandrie API](https://api-notes.eth3rnit3.org/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown or JSON-formatted command output from a Bash client] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Alexandrie password and stores authenticated session cookies in temporary files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
