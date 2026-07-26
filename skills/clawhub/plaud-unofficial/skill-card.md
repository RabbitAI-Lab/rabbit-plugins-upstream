## Description: <br>
Use when accessing Plaud voice recorder data (recordings, transcripts, AI summaries) - guides credential setup and provides patterns for plaud_client.py. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leonardsellem](https://clawhub.ai/user/leonardsellem) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users with Plaud accounts use this skill to configure credentials, list Plaud recordings, retrieve transcripts and AI summaries, and download MP3 audio through the included CLI helper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a long-lived Plaud session token locally for API access. <br>
Mitigation: Keep the `.env` file private, do not commit or share it, avoid passing tokens on the command line, and rotate or revoke the Plaud session if exposed. <br>
Risk: The CLI can access and download private recordings, transcripts, summaries, and tags. <br>
Mitigation: Use the helper only with accounts and recordings you are authorized to access, and download bulk recordings only to protected local storage you intend to retain. <br>


## Reference(s): <br>
- [Plaud API Skill Instructions](artifact/SKILL.md) <br>
- [Plaud API Reverse Engineering Documentation](artifact/PLAUD_API.md) <br>
- [Plaud Web App](https://web.plaud.ai) <br>
- [Plaud EU API Endpoint](https://api-euc1.plaud.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python CLI usage, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide API calls that list recordings, return transcript or summary JSON, and write downloaded MP3 files to local storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
