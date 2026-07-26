## Description: <br>
Verify corporate domain status to filter invalid domains, boost email deliverability, and clean CRM and email lists for exporters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams, marketers, researchers, and CRM operators use this skill to check whether corporate website domains are valid, invalid, unknown, or sensitive before outreach, supplier validation, recruitment checks, buyer verification, and email-list cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain validation uses a paid Upkuajing API and the bundled account helpers can start top-up workflows. <br>
Mitigation: Confirm current pricing and receive explicit user approval before running paid checks or creating a top-up order. <br>
Risk: The API key may be stored in a plaintext home-directory .env file. <br>
Mitigation: Prefer a managed environment variable or restrict local file permissions, and avoid storing the key on shared systems. <br>
Risk: Domain checks and version checks contact Upkuajing services and may write local version-cache data. <br>
Mitigation: Run the skill only in environments where external vendor requests and local cache writes are acceptable. <br>
Risk: API request and response logging can store queried domains and returned data locally if enabled. <br>
Mitigation: Keep API logging disabled unless local logs are required, and delete or protect logs that contain sensitive outreach or CRM data. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/upkuajing/skills/domain-validity-check) <br>
- [Domain Validity API](references/domain-api.md) <br>
- [Upkuajing Homepage](https://www.upkuajing.com) <br>
- [Upkuajing Open Platform](https://developer.upkuajing.com/) <br>
- [Upkuajing API Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON results with domain status, sensitivity status, reasons, totals, and fee information; guidance may be returned as Markdown prose with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; domain checks contact the Upkuajing API and may incur fees.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
