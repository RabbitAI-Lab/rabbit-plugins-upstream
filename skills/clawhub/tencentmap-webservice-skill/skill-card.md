## Description: <br>
Guides developers through Tencent Maps WebService HTTP APIs for geocoding, place search, route planning, distance matrices, IP location, weather, coordinate conversion, and district queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external builders use this skill to integrate Tencent Maps WebService JSON APIs into applications, select the right endpoint, generate request examples, handle API keys, and interpret service errors. It can also guide an optional temporary-key application flow when no official key is configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The temporary-key flow sends a phone number, SMS verification code, and session token to Tencent endpoints. <br>
Mitigation: Prefer an official Tencent Maps key via environment variable when possible, review the Tencent agreements before using the flow, and avoid entering real user personal data in examples. <br>
Risk: Temporary key records, including the phone number and generated key, may be written to ~/.tencentmap/tempkey.json in plaintext. <br>
Mitigation: Protect or delete the local temp-key file after testing, avoid shared machines for the temporary-key flow, and use a managed secret store for production keys. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tencent-adm/skills/tencentmap-webservice-skill) <br>
- [Tencent Maps WebService Overview](https://lbs.qq.com/service/webService/webServiceGuide/webServiceOverview) <br>
- [Tencent Maps Key Management](https://lbs.qq.com/dev/console/key/manage) <br>
- [Tencent Maps Quota Documentation](https://lbs.qq.com/dev/console/quotaImprove) <br>
- [Tencent Maps Status Codes](https://lbs.qq.com/service/webService/webServiceGuide/status) <br>
- [Geocoder API Reference](references/api-geocoder.md) <br>
- [Search API Reference](references/api-search.md) <br>
- [Direction API Reference](references/api-direction.md) <br>
- [Location and Weather API Reference](references/api-location-weather.md) <br>
- [Coordinate Tools API Reference](references/api-tools.md) <br>
- [Temporary Key Guide](tempkey-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with HTTP request examples, JSON response notes, Python helper script commands, and local configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Tencent Maps WebService key for live API calls; the optional temporary-key flow may send phone verification data to Tencent endpoints and store phone-linked key data in a local plaintext JSON file.] <br>

## Skill Version(s): <br>
1.0.1 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
