## Description: <br>
Test internet connection speed using Ookla's Speedtest CLI. Measure download/upload speeds, latency, and packet loss. Format results for social sharing on Moltbook/Twitter. Track speed history over time. Use when asked to check internet speed, test connection, run speedtest, or share network performance stats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spsneo](https://clawhub.ai/user/spsneo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and external users use this skill to run Ookla Speedtest CLI checks, format speed results for sharing, and track local network-performance history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags risky curl-to-sudo install instructions for the Ookla Speedtest CLI. <br>
Mitigation: Avoid the curl-to-sudo install path unless the installer is independently trusted and verified; prefer package-manager installation where possible. <br>
Risk: The security review flags credential-backed public posting of network-performance results. <br>
Mitigation: Use the skip option unless publishing is intended, and confirm local Moltbook or Twitter credentials and destination before posting. <br>
Risk: The security review flags local history logging of network-performance results. <br>
Mitigation: Review and manage ~/.openclaw/data/speedtest-history.jsonl according to local privacy and retention expectations. <br>


## Reference(s): <br>
- [Speedtest CLI Reference](references/speedtest-cli.md) <br>
- [Ookla Speedtest CLI Documentation](https://www.speedtest.net/apps/cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/spsneo/skills/speedtest) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text, Files] <br>
**Output Format:** [Markdown guidance with bash command examples; scripts emit terminal text, Speedtest JSON, and JSONL history records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save local history under ~/.openclaw/data/speedtest-history.jsonl and can optionally publish formatted results to Moltbook or Twitter.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
