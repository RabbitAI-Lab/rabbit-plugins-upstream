## Description: <br>
Queries a public IP geolocation service to report the current or specified public IP address, approximate location, ISP, coordinates, and timezone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunwebgo](https://clawhub.ai/user/sunwebgo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to check the active public network exit IP and approximate geolocation details for troubleshooting network, proxy, VPN, or ISP questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The external IP lookup service can observe the agent's outgoing public IP and return approximate location or ISP details in chat. <br>
Mitigation: Use only when the user wants a public-IP lookup, and avoid running it on sensitive networks unless that disclosure is acceptable. <br>
Risk: Results may reflect a VPN, proxy, carrier-grade NAT, or service-side geolocation estimate rather than the user's physical location. <br>
Mitigation: Present the result as the visible network exit and approximate geolocation, not as verified physical location. <br>
Risk: The public lookup endpoint may timeout, fail, or be unavailable. <br>
Mitigation: Return a clear failure message and do not retry repeatedly in a single conversation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunwebgo/skills/custom-ipconfig) <br>
- [ip-api.com JSON endpoint](http://ip-api.com/json/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Chinese text in a Markdown-style response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports one public-IP lookup result per conversation and avoids raw JSON output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
