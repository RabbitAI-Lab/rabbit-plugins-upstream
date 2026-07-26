## Description: <br>
Check NZBGet download status and queue information. Use when the user asks about NZBGet downloads, wants to know how many things are downloading, check download speed, view the queue, or get a full status report of their Usenet downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aricus](https://clawhub.ai/user/aricus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to query a configured NZBGet server for queue size, download speed, queue entries, and full download status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: NZBGet credentials and host access are required, and credential transport should be treated carefully. <br>
Mitigation: Install only if comfortable granting access to NZBGET_USER, NZBGET_PASS, and NZBGET_HOST; prefer localhost or a trusted LAN target, avoid untrusted networks, and consider HTTPS and curl authentication options instead of embedding credentials in the URL. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aricus/skills/nzbget) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text status summaries and concise conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queue listings are capped at 10 items; operation requires NZBGET_USER, NZBGET_PASS, and NZBGET_HOST.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
