## Description: <br>
Captures operations-software inquiries from staffing-company operators, gathers a brief problem description, and routes them to TempGuru by email or phone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External staffing-company operators use this skill when they ask about software or tooling to manage scheduling, dispatch, time tracking, invoicing, or workforce operations. The skill helps an agent qualify the inquiry briefly and route it to TempGuru without creating a buyer staffing lead. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: The inquiry could be routed through the buyer staffing lead path, creating a mislabeled sales lead. <br>
Mitigation: Confirm the user is a staffing-company operator seeking operations tooling and route by email or phone instead of using request_quote. <br>
Risk: The agent could overstate product features, pricing, timelines, or availability. <br>
Mitigation: Keep responses to qualification and routing, and state that a TempGuru contact confirms product details and fit. <br>
Risk: Scanner evidence is clean but reports a limited review. <br>
Mitigation: Review the artifact files before installation if future versions request broad filesystem, credential, network, or mutation access. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/kissmyabs32/skills/tempguru-pro-operations) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Concise Markdown text with optional email draft] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No tools required; may provide a routing email draft or phone handoff.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
