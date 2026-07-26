## Description: <br>
Compare two local documents and convert differences into LLM-ready Markdown in one synchronous call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paodingai](https://clawhub.ai/user/paodingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, document reviewers, and compliance teams use this skill to compare two local documents and receive structured Markdown differences for change review, clause comparison, downstream extraction, and rule-based validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads the selected documents and optional compare config to the configured Calliper/PDRouter SaaS API for processing. <br>
Mitigation: Use scoped API credentials, verify PD_ROUTER_BASE_URL before running, and avoid sending sensitive files unless external processing is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paodingai/skills/calliper-compare2markdown) <br>
- [PAODINGAI publisher profile](https://clawhub.ai/user/paodingai) <br>
- [Default PDRouter platform endpoint](https://platform.paodingai.com/platform/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Files, Shell commands, Configuration] <br>
**Output Format:** [Markdown diff table printed to stdout, with optional Markdown file output; non-Markdown API responses may be returned as text or formatted JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a bearer token from PAODINGAI_API_KEY or CALLIPER_ACCESS_TOKEN. The API base URL, service code, endpoint, and compare config are environment-configurable.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
