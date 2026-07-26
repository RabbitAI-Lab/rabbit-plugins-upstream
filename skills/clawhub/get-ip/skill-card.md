## Description: <br>
Gets the user's current public IP address and approximate geolocation information when asked about IP addresses, network location, or public IP checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qidu](https://clawhub.ai/user/qidu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to check a device's public IP address and approximate network location, with fallback IP lookup services when the primary service fails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The lookup sends the user's public IP address to third-party IP and geolocation services. <br>
Mitigation: Confirm user intent for vague location requests and run only when the user accepts an IP-based location check. <br>
Risk: IP-based geolocation can be approximate, incomplete, or unavailable depending on the selected service. <br>
Mitigation: Present location as approximate network-derived information and report service failures or fallback service use clearly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qidu/skills/get-ip) <br>
- [ipify API](https://api.ipify.org) <br>
- [IPinfo](https://ipinfo.io) <br>
- [icanhazip](https://icanhazip.com) <br>
- [ifconfig.me](https://ifconfig.me) <br>
- [IPIP public IP lookup](http://myip.ipip.net) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Guidance] <br>
**Output Format:** [Markdown or plain text with IP address, location, ISP, and organization fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query third-party IP lookup and geolocation services and report which fallback service succeeded.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
