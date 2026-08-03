## Description: <br>
Real phone assistant runtime with Twilio/OpenAI Realtime calling, inbound screening, confirmed outbound calls, local call logs/transcripts, optional local CRM/contact memory, calendar booking, contacts lookup, MCP tools, and a loopback-only dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[batthis](https://clawhub.ai/user/batthis) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use Amber to add real phone answering, screening, confirmed outbound calling, calendar booking, call logging, contacts lookup, and optional local CRM memory to an OpenClaw or MCP-capable agent deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amber handles real calls, transcripts, local call logs, and optional persistent caller memory. <br>
Mitigation: Use it only with caller notice and consent, access controls, retention and deletion practices, and periodic review or deletion of CRM records. <br>
Risk: Provider and gateway credentials can expose sensitive phone, AI, or OpenClaw access if reused or leaked. <br>
Mitigation: Use dedicated least-privilege Twilio, OpenAI, and OpenClaw credentials; keep secrets out of logs; rotate tokens regularly. <br>
Risk: The security evidence reports that one dashboard path stores a bridge token despite saying it stays in memory. <br>
Mitigation: Keep the dashboard loopback-only and avoid entering a bridge token until the mismatch is fixed, or rotate the token after use. <br>
Risk: Phone calls, calendar writes, and payment-related conversations can create real-world impact. <br>
Mitigation: Require explicit confirmation for outbound calls and calendar writes, disable outbound calling when not needed, and escalate payment or deposit requests to the human operator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/batthis/skills/amber-phone-agent) <br>
- [Architecture notes](artifact/references/architecture.md) <br>
- [Runtime documentation](artifact/runtime/README.md) <br>
- [Dashboard documentation](artifact/dashboard/README.md) <br>
- [Demo wizard documentation](artifact/demo/README.md) <br>
- [Interactive setup demo](https://asciinema.org/a/l1nOHktunybwAheQ) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration steps, and source code references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing setup, runtime, MCP, CRM, calendar, dashboard, and phone workflow guidance; runtime behavior also creates local logs, transcripts, and optional CRM records when configured.] <br>

## Skill Version(s): <br>
5.5.49 (source: evidence.json release.version and runtime/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
