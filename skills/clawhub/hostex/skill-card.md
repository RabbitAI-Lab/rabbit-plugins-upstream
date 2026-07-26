## Description: <br>
Hostex is an OpenAPI v3.0 skill for querying and managing vacation rental properties, room types, reservations, availability, listing calendars, guest messaging, reviews, and webhooks through the Hostex API using a PAT, with read-only defaults and optional confirmed writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ansonfreeman](https://clawhub.ai/user/ansonfreeman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and vacation-rental operators use this skill to let an agent query Hostex account data and prepare safe, intent-level Hostex API actions. Write operations are intended for explicitly approved account changes such as messages, prices, reservations, and availability updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose Hostex account data, including guest, reservation, conversation, review, and property information. <br>
Mitigation: Install it only for intended Hostex access, use a read-only or least-privilege token where possible, and avoid broad reservation or conversation retrieval unless needed. <br>
Risk: If writes are enabled, the skill can make account changes such as sending messages, changing prices, creating reservations, or updating availability. <br>
Mitigation: Keep HOSTEX_ALLOW_WRITES unset except for a specific approved change, review dry-run or planned write output, and require explicit confirmation before execution. <br>
Risk: A custom Hostex base URL could send requests to an untrusted endpoint. <br>
Mitigation: Do not set HOSTEX_BASE_URL unless it points to a trusted Hostex endpoint. <br>


## Reference(s): <br>
- [Hostex OpenAPI v3 config](https://hostex.io/open_api/v3/config.json) <br>
- [Cached OpenAPI schema](references/openapi.json) <br>
- [ClawHub skill page](https://clawhub.ai/ansonfreeman/skills/hostex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read commands return Hostex API JSON; guarded write commands print planned changes unless writes are enabled and confirmed.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
