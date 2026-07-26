## Description: <br>
RedFoxHub helps an agent search and read RedFoxHub data through the OOMOL redfox connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to search and retrieve Douyin, WeChat Official Accounts, TikTok, and Xiaohongshu account, work, article, and AI-creation data through an OOMOL-connected RedFoxHub account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use the user's OOMOL-connected RedFoxHub account for lookups. <br>
Mitigation: Install and enable it only when that account-scoped RedFoxHub access is intended. <br>
Risk: First-time setup may require installing or authenticating the OOMOL oo CLI. <br>
Mitigation: Run installer, login, or connection steps only after relevant command failures and only when the OOMOL CLI installation path is trusted. <br>
Risk: Future connector actions could be marked write or destructive. <br>
Mitigation: Fetch the live action schema, review the payload and effect, and require explicit user confirmation before any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub RedFoxHub skill page](https://clawhub.ai/oomol/skills/oo-redfox) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [RedFoxHub homepage](https://redfox.hk) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
