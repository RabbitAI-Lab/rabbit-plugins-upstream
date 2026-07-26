## Description: <br>
Daily digest of the Bitcoin Development mailing list and Bitcoin Core commits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawd21](https://clawhub.ai/user/clawd21) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, Bitcoin contributors, and technically curious readers use this skill to get concise daily summaries of bitcoin-dev mailing list activity and Bitcoin Core commits, with links back to the original public sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public content from Google Groups, GitHub, and gnusha.org. <br>
Mitigation: Install only in environments where those public network requests are acceptable, and review generated summaries against linked sources for important decisions. <br>
Risk: The digest command writes local archives under ~/workspace/bitcoin-dev-archive. <br>
Mitigation: Review local storage expectations before enabling the skill, and manage or delete archived files according to workspace retention needs. <br>
Risk: Daily cron creates recurring fetches and recurring local storage. <br>
Mitigation: Enable the cron only when recurring summaries are desired, and disable it if daily network activity or archive growth is not acceptable. <br>


## Reference(s): <br>
- [Bitcoin Development mailing list](https://groups.google.com/g/bitcoindev) <br>
- [Bitcoin Core commits](https://github.com/bitcoin/bitcoin/commits/master/) <br>
- [Bitcoin Development public-inbox mirror](https://gnusha.org/pi/bitcoindev/) <br>
- [ClawHub skill page](https://clawhub.ai/clawd21/skills/bitcoin-daily) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown summaries with source links, command-line text output, and local JSON or Markdown archive files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Archives raw mailing list threads, commit data, and generated summaries under ~/workspace/bitcoin-dev-archive when the digest command runs.] <br>

## Skill Version(s): <br>
1.3.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
