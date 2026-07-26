## Description: <br>
BaseMail gives AI agents a Base-linked email identity for SIWE wallet authentication, sending email, and receiving confirmations through the BaseMail API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use BaseMail to give an AI agent a verifiable @basemail.ai mailbox tied to a Base wallet or Basename, then register, send messages, and read inbox confirmations autonomously. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can request wallet-signing authority during registration and can access a BaseMail mailbox through stored or supplied credentials. <br>
Mitigation: Use a dedicated low-value wallet, restrict access to BASEMAIL_PRIVATE_KEY and BASEMAIL_TOKEN, and review the ~/.basemail directory for encrypted keys and cached tokens before and after use. <br>
Risk: Managed setup may display sensitive recovery material or prompt for wallet passwords in terminal sessions that could be logged. <br>
Mitigation: Avoid managed setup in CI or recorded terminals, treat displayed mnemonics and echoed passwords as secrets, and prefer an existing wallet supplied through a controlled environment variable or wallet file. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/daaab/skills/basemail) <br>
- [BaseMail Website](https://basemail.ai) <br>
- [BaseMail API Documentation](https://api.basemail.ai/api/docs) <br>
- [BaseMail API](https://api.basemail.ai) <br>
- [Basenames](https://www.base.org/names) <br>
- [Base Chain](https://base.org) <br>
- [Source Repository](https://github.com/dAAAb/BaseMail-Skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and API-oriented workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and BaseMail credentials; registration may use BASEMAIL_PRIVATE_KEY, while send and inbox operations can use a cached token.] <br>

## Skill Version(s): <br>
1.8.1 (source: server release evidence; artifact frontmatter and package.json report 1.8.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
