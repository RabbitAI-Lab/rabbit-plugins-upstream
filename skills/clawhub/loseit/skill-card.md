## Description: <br>
Read-only Lose It nutrition extractor that authenticates with a user's Lose It credentials or an export ZIP, fetches the user's data export, and emits per-day nutrition as JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stozo04](https://clawhub.ai/user/stozo04) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to retrieve their own Lose It nutrition history as structured per-day JSON for downstream analysis, logging, or personal automation. It is intended for read-only extraction of nutrition data, not for modifying a Lose It account or storing application state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Lose It exports and nutrition JSON that may contain personal health data. <br>
Mitigation: Treat exported ZIPs and nutrition output as sensitive data; avoid sharing, logging, syncing, or backing them up unless the user explicitly intends that. <br>
Risk: The skill can read plaintext Lose It credentials from config.json and cache a reusable session token locally. <br>
Mitigation: Prefer environment variables or the --zip flow on shared machines, keep config.json private, and store the token cache only in an owner-only local directory. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/stozo04/skills/loseit) <br>
- [Source Repository](https://github.com/stozo04/loseit-cli) <br>
- [README](artifact/README.md) <br>
- [Agent Contract](artifact/AGENTS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [JSON nutrition objects on stdout, with setup and command guidance in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The core days command emits a JSON object keyed by ISO date; human hints and errors are kept on stderr.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
